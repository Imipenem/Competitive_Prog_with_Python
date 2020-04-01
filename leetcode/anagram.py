def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def anagramII(s,t):
    s_dict = {}
    for c in s:
        if c not in s_dict: s_dict[c] = 1
        else: s_dict[c] += 1
    for c in t:
        if c not in s_dict: return False
        else:
            s_dict[c] -= 1
            if s_dict[c] == 0: del s_dict[c]
    return not(s_dict)

# Third option would be to use collections.Counter()

if __name__ == "__main__":
	print(isAnagram("rat","car"))
