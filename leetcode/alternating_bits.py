#bit messy bit it works lol
def hasAlternatingBits(n: int) -> bool:
    return int(bin(n^1431655765)[-len(bin(n))+1:],2)==0 or int(bin(n^2863311530)[-len(bin(n))+2:],2)==0

#sometimes more straightforward is easier lol
def hasAlternatingBitsII(n: int) -> bool:
    bits = bin(n)
    len = len(bits)
    return all(bits[i] != bits[i+1] for i in range(len-1))

if __name__ == '__main__':
    print(hasAlternatingBits(2147483646))
    print(hasAlternatingBits(2))
    print(hasAlternatingBits(0))
    print(hasAlternatingBits(10))

