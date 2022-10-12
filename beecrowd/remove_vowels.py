def main():
    string: str = 'Practice Problems to Drill List Comprehension in Your Head.'

    print(solve(string))


def solve(s: str) -> str:
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    
    return ''.join([x for x in s if x.lower() not in vowels])


if __name__ == '__main__':
    main()