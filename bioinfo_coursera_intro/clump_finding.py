from collections import Counter

def ClumpFinding(genome, k, L, t):
    """
        Search for the most frequent K-mers (patterns in the genome of length k)
    """
    c = Counter([genome[i: i + k] for i in range(0, (L + 1) - k)])
    print(c)

    setOfMostFrequentKmers = set()
    for key, value in c.items():
        if value >= t:
            setOfMostFrequentKmers.add(key)

    for i in range(L, (len(genome) + 1) - k):
        substract = genome[i-L:(i-L)+k]
        c[substract] -= 1

        add = genome[i-k+1:i+1]
        if add in c:
            c[add] += 1
            if c[add] >= t and add not in setOfMostFrequentKmers:
                setOfMostFrequentKmers.add(add)

        else:
            c[add] = 1

    return setOfMostFrequentKmers

if __name__ == '__main__':
    print()