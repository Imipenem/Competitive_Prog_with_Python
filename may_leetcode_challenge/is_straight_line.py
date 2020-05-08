# LEETCODE May Challenge Day 8


def checkStraightLine(coordinates: [[]]) -> bool:
    s_x, s_y = coordinates[0][0], coordinates[0][1]  # starting point coordinates
    x_diff, y_diff = coordinates[1][0] - s_x, coordinates[1][1] - s_y  # ratio of first two points (derivation)
    if not y_diff:
        x_y_ratio = 0
    else:
        x_y_ratio = x_diff/y_diff

    for p in coordinates[2:]:
        if not p[1] - s_y:
            if x_y_ratio != 0:
                return False
        elif (p[0] - s_x)/(p[1] - s_y) != x_y_ratio:
            return False
    return True


if __name__ == '__main__':
    print(checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))