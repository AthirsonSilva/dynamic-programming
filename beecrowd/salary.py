def main():
    a: int = int(input())
    b: int = int(input())
    c: float = float(input())

    r: dict = solve(a, b, c)

    print('NUMBER = %i' %r['number'])
    print('SALARY = U$ %0.2f' %r['salary'])


def solve(a: int, b: int, c: float) -> dict:
    r: dict = {
        'number': a,
        'salary': round(float(b * c), 2)
    }  
    
    return r


if __name__ == '__main__':
    main()