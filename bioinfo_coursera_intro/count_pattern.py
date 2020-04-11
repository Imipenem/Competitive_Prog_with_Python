import re
import timeit
from collections import Counter

"""
Various function for counting the number of occurences of a specific pattern in a DNA string
"""


def count_pattern(genome: str, pattern: str) -> int:
    """
    Medium (half the time of counter like 9.5 sec for 10000 runs like below)
    """
    count = 0

    for i in range(0, len(genome) + 1 - len(pattern)):
        if genome[i: i + len(pattern)] == pattern:
            count += 1
    return count


def count_pattern_with_re(genome: str, pattern: str) -> int:
    """
    Very fast (0.34 sec for 10000 runs like below)
    NO OVERLAPPS COUNTING
    """
    matches = re.finditer(pattern,genome)
    results = [str(match.group(0)) for match in matches]
    return len(results)


def count_pattern_with_counter(genome: str, pattern: str) -> int:
    """
    Very slow (21 sec for 10000 runs like below)
    """
    c = Counter([genome[i: i + len(pattern)] for i in range(0, len(genome) - len(pattern))])
    return c[pattern]


if __name__ == '__main__':
    print(count_pattern("GCGCG","GCG"))
# timeit statement
# stmt were calls to above three functions
# print(timeit.timeit(setup="from __main__ import count_pattern",stmt=mycode, number=10000))

# print(timeit.timeit(setup="from __main__ import count_pattern_with_re\nimport re",stmt=mycode2, number=10000))

# print(timeit.timeit(setup="from __main__ import count_pattern_with_counter\nfrom collections import Counter",stmt=mycode3, number=10000))
