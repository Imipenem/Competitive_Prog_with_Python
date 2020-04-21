def computeReverse(strand: str) -> str:
    """
    God I love Python: Compute Reverse complement strand for given DNA string
    :param strand: Given DNA string
    :return: Reverse complement string
    """
    return ''.join({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[strand[i]] for i in range(len(strand)))[::-1]


if __name__ == '__main__':
    print(computeReverse("GATTACA"))