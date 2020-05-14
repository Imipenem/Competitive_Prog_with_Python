# 1015. Smallest Integer Divisible by K
# Given an integer K, find the smallest integer containing only 1´s that is divisible by K. I none return -1, else its length.
# We need to store only remainders

def smallestRepunitDivByK(K: int) -> int:
    l, s = 1, 0
    if K % 2 == 0 or K % 5 == 0:
        return -1

    while True:
            s = (s*10+1) % K
            if not s: return l
            l += 1


if __name__ == '__main__':
    print(smallestRepunitDivByK(2))