from collections import Counter


def count_pattern_with_counter(genome: str, k: int) -> list:
    """
    Search for the most frequent K-mers (patterns in the genome of length k)
    """
    c = Counter([genome[i: i + k] for i in range(0, (len(genome) + 1) - k)])
    itemMaxValue = max(c.items(), key=lambda x: x[1])

    listOfMostFrequentKmers = list(itemMaxValue)
    for key, value in c.items():
        if value == itemMaxValue[1]:
            listOfMostFrequentKmers.append(key)
    return listOfMostFrequentKmers


if __name__ ==  '__main__':
    print(count_pattern_with_counter("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",3))