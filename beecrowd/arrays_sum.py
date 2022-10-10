def main():
    a: list[int] = [int(input()) for i in range(0, 10)]
    b: list[int] = [int(input()) for i in range(0, 10)]

    print(*(x for x in solve(a, b)))


def solve(a: list[int], b: list[int]) -> list[int]:
    zipped: zip[tuple[int, int]] = zip(a, b)    

        
    return [x + y for (x, y) in zipped]


if __name__ == '__main__':
    main()