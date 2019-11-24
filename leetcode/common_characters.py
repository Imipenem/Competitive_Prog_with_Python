#1002. Find Common Characters
def commonChars(A) -> [str]:
    hs = {c: A[0].count(c) for c in A[0]}

    for char in hs.keys():
        for st in A:
            if st.count(char) < hs.get(char): hs[char] = st.count(char)

    return list((''.join([char*occ for char,occ in hs.items() if occ > 0])))



if __name__ == "__main__":
    print(commonChars(["bella","roller"]))
