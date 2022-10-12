def main():
    nums: list[int] = [x for x in range(1, 1001)]

    print(solve(nums))


def solve(nums: list[int]) -> dict:
    return {
        num: max([divisor for divisor in range(1, 10) if num % divisor == 0])
        for num in nums
    }


if __name__ == '__main__':
    main()