def main():
    string: str = 'Practive problems to Drill List Comprehension in Your Head.'

    print(solve(string))


def solve(string: str) -> dict[str, int]:
    return {x: len(x) for x in string.split()}


if __name__ == '__main__':
    main()
