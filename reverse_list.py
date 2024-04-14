from typing import TypeVar
import copy as cp
import rainbow

T = TypeVar("T")
N = TypeVar("N", int, float)


def assert_lists_reversed(fwd: list[T], rev: list[T]) -> None:
    assert len(fwd) == len(rev)
    for i in range(len(fwd)):
        assert fwd[i] == rev[-(1 + i)]


def stepped_list_reverse(fwd: list[N]) -> list[N]:
    rev = cp.copy(fwd)
    length = len(fwd)
    print(rainbow.purple(f"{fwd=} {rev=}"))
    for index in range(length):
        item = fwd[-(1 + index)]
        current = rev[index]
        print(rainbow.lightgrey(f"comparing {item=} to {current=}"))
        while item != current:
            if item < current:
                print(rainbow.lightgrey("split"))
                rev[index] = item
                rev.insert(index + 1, current - item)
            elif item > current:
                next_ = rev[index + 1]
                print(rainbow.lightgrey("merge"))
                rev[index] = next_ + current
                del rev[index + 1]
            print(f"{fwd=} {rev=}")
            current = rev[index]
    return rev


def main() -> None:
    forward_list = [5, 7, 1]
    reverse_list = stepped_list_reverse(forward_list)
    assert_lists_reversed(forward_list, reverse_list)
    print(rainbow.cyan(80 * "*"))
    forward_list = [1, 1, 4, 3]
    reverse_list = stepped_list_reverse(forward_list)
    assert_lists_reversed(forward_list, reverse_list)


if __name__ == "__main__":
    main()
