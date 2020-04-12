import urllib.request
import timeit
import re


def vibrio_cholerae_pattern_re():
    genome = urllib.request.urlopen("https://stepik.org/media/attachments/lessons/3/Vibrio_cholerae.txt").read()
    return match_with_re("CTTGATCAT", genome.decode('utf-8'))


def vibrio_cholerae_pattern_naiv():
    genome = urllib.request.urlopen("https://stepik.org/media/attachments/lessons/3/Vibrio_cholerae.txt").read()
    return pattern_matching("CTTGATCAT", genome.decode('utf-8'))


def pattern_matching(pattern: str, genome: str) -> str:
    match = []
    k = len(pattern)

    for i in range(len(genome) + 1 - k):
        if genome[i: i+k] == pattern:
            match.append(i)
    return ' '.join([str(match[i]) for i in range(len(match))])


def match_with_re(pattern: str, genome: str) -> str:
    matches = [m.start(0) for m in re.finditer(pattern, genome)]
    return ' '.join([str(matches[i]) for i in range(len(matches))])


if __name__ == '__main__':
    setup_naiv = "from __main__ import pattern_matching\nfrom __main__ import vibrio_cholerae_pattern_naiv\n" \
            "import urllib.request"

    setup_re = "from __main__ import pattern_matching\nfrom __main__ import vibrio_cholerae_pattern_re\n" \
            "import urllib.request\nimport re"

    code_naiv = "vibrio_cholerae_pattern_naiv()"

    code_re = "vibrio_cholerae_pattern_re()"

    print(timeit.timeit(setup=setup_naiv,stmt=code_naiv, number=1))

    print(timeit.timeit(setup=setup_re, stmt=code_re, number=1))
