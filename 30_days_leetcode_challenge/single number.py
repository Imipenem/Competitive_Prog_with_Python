def singleNumber(nums: list) -> int:
    res = nums[0]
    for i in range(1, len(nums)):
        res ^= nums[i]
    return res


if __name__ == '__main__':
    print(singleNumber([2,0,0]))
