import argparse
import numpy as np
from scipy.spatial import Voronoi  # , voronoi_plot_2d
import matplotlib.pyplot as plt


def average_voronoi_perimeters(
    point_count: int = 10,
    samples: int = 10,  #  , plot: bool = False
) -> None:
    """
    Generate Voronoi graphs for 1 to point_count random points in the range [0,1].
    Calculate the sum of the perimeters then average over N samples.
    The perimeters are bounded by the bounding box [0,0,1,1].
    """
    perimeters = {i: [] for i in range(point_count)}
    for i in range(samples):
        new_point = np.random.random(2)
        # Reflect the points around the edges of the bounding box.
        # This creates region edges aligned with the bounding box.
        points = np.array(
            [
                new_point,
                new_point * [1, -1],
                new_point * [-1, 1],
                new_point * [1, -1] + [0, 2],
                new_point * [-1, 1] + [2, 0],
            ]
        )
        voronoi = Voronoi(points, incremental=True)
        perimeters[0].append(4)
        for j in range(1, point_count):
            new_point = np.random.random(2)
            points = np.array(
                [
                    new_point,
                    new_point * [1, -1],
                    new_point * [-1, 1],
                    new_point * [1, -1] + [0, 2],
                    new_point * [-1, 1] + [2, 0],
                ]
            )
            voronoi.add_points(points)
            # if plot:
            #     fig = voronoi_plot_2d(voronoi)
            #     plt.axis([0, 1, 0, 1])
            #     plt.show()
            #     # fig = voronoi_plot_2d(voronoi)
            #     # plt.show()
            perimeters[j].append(0)
            for region in voronoi.regions:
                if len(region) == 0:
                    continue
                if any([r < 0 for r in region]):
                    continue
                shape = np.array([voronoi.vertices[x] for x in region])
                if (shape > 1 + 1e-10).any():
                    continue
                if (shape < -1e-10).any():
                    continue
                perimeter = np.linalg.norm(
                    np.roll(shape, 1, axis=0) - shape, axis=1
                ).sum()
                perimeters[j][-1] += perimeter
    values = []
    for key, perimeter in perimeters.items():
        average_perimeter = np.array(perimeter).mean()
        values.append([key + 1, average_perimeter])
        print(f"{key + 1}: {average_perimeter}")
    values = np.array(values)
    plt.plot(values[:, 0], values[:, 1])
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="voronoi_perimeter",
        description="Calculates the average permiter of Voronoi segments for N points",
    )
    parser.add_argument(
        "-c",
        "--max_point_count",
        type=int,
        default=10,
        help="maximum number of points to add",
    )
    parser.add_argument(
        "-n",
        "--samples",
        type=int,
        default=10,
        help="Number of samples to average over",
    )
    # parser.add_argument(
    #     "-p",
    #     "--plot",
    #     action="store_true",
    #     help="Plot the Voronoi diagrams",
    # )
    args = parser.parse_args()

    average_voronoi_perimeters(args.max_point_count, args.samples)  #  , args.plot)
