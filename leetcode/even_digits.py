def findNumbers(nums: [int]) -> int:
    return len(list(([e for e in nums if len(str(e))%2 == 0])))

if __name__ == '__main__':
    print(findNumbers([12,345,2,6,7896]))

