def minDistance(word1: str, word2: str) -> int:
    if not word1 or not word2: return max(len(word1), len(word2))  # at least one string is empty

    dp_table = [[0 for col in range(len(word1)+1)] for row in range(len(word2)+1)]

    # init with edit distance for substr[0,i] for 0<= i <= len(word1 and word2)
    dp_table[0] = list(range(0, len(word1) + 1))
    for i in range(1,len(word2) + 1):
        dp_table[i][0] = i

    # now choose minimum edit distance from the three option delete/replace/insert
    # if chars are the same -> edit distance is the same as for those substring without these chars of word1 and word2

    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            # choose minimum edit distance from delete, replace or insert at current substring problem
            if word1[j-1] == word2[i-1]:
                dp_table[i][j] = dp_table[i-1][j-1]
            else:dp_table[i][j] = min(min(dp_table[i][j-1], dp_table[i-1][j-1]), dp_table[i-1][j]) + 1

    return dp_table[len(word2)][len(word1)]





if __name__ == "__main__":
    print(minDistance("intention", "execution"))