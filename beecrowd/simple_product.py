def main():
    A: int = int(input())
    B: int = int(input())

    Product: int = solve(A, B)

    print(f'PROD = {Product}')


def solve(A: int, B: int) -> int:
    return int(A * B)


if __name__ == '__main__':
    main()
