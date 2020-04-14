def stringShift(s: str, shift) -> str:
    length = len(s)
    s = s
    for shift_op in shift:
        s = s[length - (shift_op[1] % length):] + s[0:length - (shift_op[1]) % length] if shift_op[0] else s[shift_op[1] % length:length]+s[:shift_op[1] % length]
    return s


if __name__ == "__main__":
    print(stringShift("abcdefg",[[1,3]]))
