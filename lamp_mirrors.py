import json
import math

SCENE = {
  "version": 5,
  "objs": [],
  "width": 1000,
  "height": 1000,
  "rayModeDensity": 0.99,
  "origin": { 
    "x": 500,
    "y": 1000,
  },
  "scale": 1.5
}


def add_points(objs: list, N: int = 8) -> None:
    x = -4
    for i in range(N+1):
        point = {
              "type": "PointSource",
              "x": x,
              "y": 0,
            }
        x += 1
        objs.append(point)


def add_mirrors(objs: list, angle: float= 52) -> None:
    swap_angle = 180 - angle
    length = 2
    points = (
        ((-5, 1), (-5, -1)),
        ((5, 1), (5, -1)),
        ((-5, -1), (5, -1)),
        ((5, 1), (5 + length*math.cos(angle/180*math.pi), 1+ length*math.sin(angle/180*math.pi))),
        ((-5, 1), (-5 + length*math.cos(swap_angle/180*math.pi), 1+ length*math.sin(swap_angle/180*math.pi))),
    )
    for p1, p2 in points:
        mirror = {
              "type": "Mirror",
              "p1": {
                "x": p1[0],
                "y": -p1[1],
              },
              "p2": {
                "x": p2[0],
                "y": -p2[1],
              }
            }
        objs.append(mirror)

    

def add_detector(objs: list, bins: int=5) -> None:
    x = -100
    y = 500
    detector = {
          "type": "Detector",
          "p1": {
            "x": x,
            "y": -y,
          },
          "p2": {
            "x": x+200,
            "y": -y,
          },
          "irradMap": True,
          "binSize": bins,
        }
    objs.append(detector)


def main():
    objs = []
    add_points(objs)
    add_mirrors(objs)
    add_detector(objs)
    SCENE["objs"] = objs
    with open("plotlogic_light.json", "w") as fid:
        json.dump(SCENE, fid)


if __name__ == "__main__":
    main()
