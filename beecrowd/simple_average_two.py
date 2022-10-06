def main():
    a, b, c = map(float, input().split())

    result = solve(a, b, c)

    print('MEDIA = %0.1f' % result)


def solve(a: float, b: float, c: float) -> float:
    return float((a * 2 + b * 3 + c * 5) / (2 + 3 + 5))


if __name__ == '__main__':
    main()
