def main():
    s: str = str(input())

    print(solve(s))


def solve(s: str) -> str:
    r: str = str(s[::-1])
    print(f'Reverse = {r}')
    print(f'Normal = {s}')

    if r == s:
        return 'Palíndromo'

    return 'Não é palíndromo'


if __name__ == '__main__':
    main()
