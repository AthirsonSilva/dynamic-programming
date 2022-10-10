def main():
    nums: list[int] = [i for i in range(1, 1001)]
    
    print(*(x for x in solve(nums)))


def solve(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 8 == 0]



if __name__ == '__main__':
    main()
    