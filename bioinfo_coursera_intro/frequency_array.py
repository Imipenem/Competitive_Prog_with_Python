basic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
basic2 = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

"""
Basic note: Remember that within DNA (4 bases) there are 4^k possible strings of length k (permutations).
So for distribution: For example one would expect a 3-mer occuring every 4^3 bases or a 8-mer every 4^8 bases.
"""

def pattern_to_number(seq: str) -> int:
    """
    Convert a DNA string to number (index in a freq array)
    :param seq: The given DNA string
    :return: Index of string in freq array
    """
    if not seq:
        return 0
    return 4 * pattern_to_number(seq[:-1]) + basic[seq[-1]]


def NumberToPattern(index, k) -> str:
    """
    Convert index of freq array to DNA string
    :param index: Index in the frequency array
    :param k: length of result DNA string
    :return: The encoded DNA string from the given index of length k
    """
    if index == 0: return k * "A"
    return NumberToPattern(int(index / 4), k-1) + basic2[index % 4]


if __name__ == '__main__':
    print(NumberToPattern(5437, 8))
