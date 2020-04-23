def rangeBitwiseAnd(m: int, n: int) -> int:
    cnt = 0
    while m != n:
        m >>= 1
        n >>= 1
        cnt += 1
    return n << cnt

if __name__ == '__main__':
    print(rangeBitwiseAnd(5,7))
