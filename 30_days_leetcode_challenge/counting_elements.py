from collections import Counter


def countElements(arr) -> int:
    cnt = Counter(arr)
    res = 0
    for key in cnt:
        if key + 1 in cnt.keys():
            res += cnt[key]
    return res


if __name__ == "__main__":
    print(countElements([]))
