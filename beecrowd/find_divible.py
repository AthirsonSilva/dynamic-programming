def main():
    array: list[int] = [x for x in range(1, 1001)]

    print(*(solve(array)))


def solve(l: list[int]) -> list[int]:
    return [x for x in l if True in [True for y in range(2, 10) if x % y == 0]]


if __name__ == '__main__':
    main()
