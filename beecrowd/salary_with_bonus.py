def main():
    n: str = str(input())
    f: float = float(input())
    s: float = float(input())
    
    
    r: float = solve(f, s)

    print('TOTAL = R$ %0.2f' %r)


def solve(f: float, s: float) -> float:
    t: float = (s * 0.15) + f
    
    return t


if __name__ == '__main__':
    main()