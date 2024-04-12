from typing import TypeVar
import copy as cp

T = TypeVar("T")
N = TypeVar("N", int, float)


def assert_lists_reversed(fwd: list[T], rev: list[T]) -> None:
    assert len(fwd) == len(rev)
    for i in range(len(fwd)):
        assert fwd[i] == rev[-(1 + i)]


def stepped_list_reverse(fwd: list[N]) -> list[N]:
    rev = cp.copy(fwd)
    length = len(fwd)
    print(f"{fwd=} {rev=}")
    for index in range(length):
        item = fwd[-(1 + index)]
        current = rev[index]
        print(f"comparing {item=} to {current=}")
        while item != current:
            if item < current:
                print("split")
                rev[index] = item
                rev.insert(index + 1, current - item)
            elif item > current:
                next_ = rev[index + 1]
                if next_ + current <= item:
                    print("merge")
                    rev[index] = next_ + current
                    del rev[index + 1]
                elif next_ + current > item:
                    print("split + merge")
                    rev[index] = item
                    rev[index + 1] = next_ + current - item
            print(f"{fwd=} {rev=}")
            current = rev[index]
    return rev


def main() -> None:
    forward_list = [5, 7, 1]
    reverse_list = stepped_list_reverse(forward_list)
    assert_lists_reversed(forward_list, reverse_list)
    forward_list = [1, 1, 4, 3]
    reverse_list = stepped_list_reverse(forward_list)
    assert_lists_reversed(forward_list, reverse_list)


if __name__ == "__main__":
    main()
