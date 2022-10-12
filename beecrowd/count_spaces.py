def main():
    ns: list[int] = [x for x in range(1, 1001)]
    string: str = 'Practive Problems to Drill List Comprehension in Your Head.'

    print(solve(string))

def solve(ns: str) -> int:
    return len([x for x in ns if str(x) == ' '])


if __name__ == '__main__':
    main()