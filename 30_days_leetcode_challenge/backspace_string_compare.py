def backspaceCompare(S: str, T: str) -> bool:
    return do_backwards(S, "", 0) == do_backwards(T, "", 0)


def do_backwards(string, add_to, counter):
    for c in reversed(string):
        if c == '#':
            counter += 1
        else:
            if counter == 0:
                add_to += c
            else:
                counter -=1
    return add_to


if __name__ == "__main__":
    print(backspaceCompare("a#c", "b"))