# 1347. Minimum Number of Steps to Make Two Strings Anagram
# Given to strings s and t, determine min number of steps required to make t an anagram of s
from collections import Counter


def minSteps(s: str, t: str) -> int:
    s_c, t_c = Counter(s), Counter(t)
    res = 0

    for key in t_c.keys():
        if key in s_c:
            res += abs(s_c[key] - t_c[key])
        else:
            res += t_c[key]

    for key in s_c.keys():
        if key not in t_c:
            res += s_c[key]

    return int(res/2)


if __name__ == '__main__':
    print(minSteps("friend", "family"))
