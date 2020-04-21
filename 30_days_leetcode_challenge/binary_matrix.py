def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    idx = -1
    dimensions = binaryMatrix.dimensions()
    rows = dimensions[0]
    cols = dimensions[1]

    row = 0  # coordinates to start at top right
    col = cols-1

    while row != rows and col != -1:
        if binaryMatrix.get(row, col):
            idx = col
            col -= 1
        else:
            row += 1

    if row == rows and col != 0:
        for i in range(col,-1,-1):
            if binaryMatrix.get(row-1,i):
                idx = i
            else:
                return idx

    return idx
