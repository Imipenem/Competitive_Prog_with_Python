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


if __name__ == "__main__":
    print(computeFuel())