def main():
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    d: int = int(input())
    
    result: int = solve(a, b, c, d)

    print('DIFERENCA = %i' %result)

def solve(a: int, b: int, c: int, d: int) -> int:
    return int((a * b) - (c * d))


if __name__ == '__main__':
    main()