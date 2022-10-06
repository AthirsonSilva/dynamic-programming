def main():
    A, B = map(float, input().split())

    AVG: float = solve(A, B)

    print('MEDIA = %0.5f' % AVG)


def solve(A: float, B: float) -> float:
    return float(((A * 3.5) + (B * 7.5)) / (3.5 + 7.5))


if __name__ == '__main__':
    main()
