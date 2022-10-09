def main():
    while True:
        p: float = float(input())
        l: float = float(input())

        print(solve(p, l))

        try:
            q: str = str(input('Continue? [y/ n]').lower())

            if str(q) == 'n':
                break
            
        except:
            print('Invalid answer')


def solve(p: float, l: float) -> float:
    return float(p + (p * (l / 100)))


if __name__ == '__main__':
    main()