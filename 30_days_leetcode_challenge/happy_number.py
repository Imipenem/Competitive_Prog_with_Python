def isHappy(n: int) -> bool:
    res, num = 0, n
    while True:
        while num > 0:
            res += (num % 10)**2
            num = int(num / 10)
        if res == 1: return True
        elif res == 4: return False
        num = res
        res = 0


if __name__=="__main__":
    print(isHappy(145))