import collections.Counter

def countCharacters(words: [str], chars: str) -> int:
    sum = 0
    template = Counter(chars)

    for word in words:
        mark = True
        hs = Counter(word)
        for key in hs:
            if key in template:
                if hs[key] > template[key]:
                    mark = False
                    break
            else:
                mark = False
                break

        if mark:sum += len(word)
    return sum

if '__name' == '__main__':
    print()
