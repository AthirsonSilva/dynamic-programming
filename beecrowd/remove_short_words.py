def main():
    string: str = 'Practive Problems to Drill List Comprehension in Your Head.'

    print(solve(string))


def solve(string: str) -> list[str]:
    return [x for x in string.split() if len(x) < 5]


if __name__ == '__main__':
    main()