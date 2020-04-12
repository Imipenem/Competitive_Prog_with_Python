import bisect


def lastStoneWeight(stones: list) -> int:
    stones = sorted(stones)
    while len(stones) > 1:
        smash = abs(stones[-1] - stones[-2])
        stones = stones[:-2]
        if smash > 0:
            bisect.insort(stones, smash)

    if len(stones) == 1: return stones[0]
    return 0


if __name__ == '__main__':
    print()
