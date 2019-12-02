"""
Advent Of Code 1.1
"""
def computeFuel():
    sum,cnt = 0,0
    with open("/home/thelichking/Desktop/adventOfCode/Day1/Input Puzzle 1.1", 'r') as f:
        number = f.readline()
        while number:
            try:
                sum += int(int(number.replace("\n", "")) / 3 - 2)
                number = f.readline()
            except:break
    return sum


"""
Advent Of Code 1.2
"""
def computeFuelII():
    sum,cnt = 0,0
    with open("/home/thelichking/Desktop/adventOfCode/Day1/Input Puzzle 1.1", 'r') as f:
        number = f.readline()
        while number:
            try:
                sum += computeFuelRec(int(number.replace("\n", "")),0)
                number = f.readline()
            except:break
    return sum


def computeFuelRec(num, sum) -> int:
    if num < 9: return sum
    temp = int(num / 3) - 2
    sum += temp
    return computeFuelRec(temp, sum)


if __name__ == "__main__":
    print(computeFuelII())