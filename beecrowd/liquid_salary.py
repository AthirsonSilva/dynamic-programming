def main():
    v: float = float(input())
    a: int = int(input())

    print(solve(v, a))


def solve(v: float, a: int) -> float:
    s: float = a * v
    print(s)
    
    if s <= 1_212:
        print(1)
        return float(s * 0.75)
    
    elif s <= 2_427.35:
        print(2)
        return float(s * 0.9)
    
    elif s <= 3_641.03:
        print(3)
        return float(s * 1.2)
    
    elif s <= 7_087.23:
        print(4)
        return float(s * 1.4)
    
    elif s <= 12_136.80:
        print(5)
        return float(s * 1.45)
    
    elif s <= 24_273.58:
        print(6)
        return float(s * 1.65)
    
    elif s <= 47_33.46:
        print(7)
        return float(s * 1.9)
    
    print(8)
    return float(s - (s * 0.22))
    


if __name__ == '__main__':
    main()