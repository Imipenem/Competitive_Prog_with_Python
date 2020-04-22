def subarraySum(nums: [int], k: int) -> int:
    map = {0: 1}  # we saw sum 0 one time, thus at the very beginning
    sum, cnt = 0, 0

    for i in range(len(nums)):
        sum += nums[i]
        cnt += map.get(sum-k, 0)  # get the number of arrays with sum 'sum-k' we've seen so far
        map[sum] = map.get(sum, 0) + 1  # increment by one
    return cnt


if __name__ == '__main__':
    print(subarraySum([1,1,1],2))