def main():
    ns: list[int] = [x for x in range(1, 1001)]

    print(*solve(ns))

def solve(ns: list[int]) -> list[int]:
    return [n for n in ns if str(n).find('6') == True]


if __name__ == '__main__':
    main()