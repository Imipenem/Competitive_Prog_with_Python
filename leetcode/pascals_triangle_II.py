
def getRow(rowIndex: int) -> [int]:
    if rowIndex < 2: return [1] * (rowIndex + 1)
    lst = [1] * (rowIndex+1)

    small = int(rowIndex/2)
    comb = 1
    j = 1

    for i in range(rowIndex,small-1,-1):
        comb = (comb*i)/j
        j+=1
        lst[i-1] = int(comb)
        lst[j-1] = int(comb)
    return lst



if __name__ == '__main__':
    print(getRow(5))

