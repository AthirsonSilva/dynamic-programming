R: float = float(input())
n: float = 3.14159


def main():
    A: float = solve(R)
    print("A=%0.4f" % A)


def solve(R: float) -> float:
    return n * (R**2)


if __name__ == '__main__':
    main()
