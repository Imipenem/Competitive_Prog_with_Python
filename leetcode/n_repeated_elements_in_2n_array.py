#961. N-Repeated Element in Size 2N Array: An O(n) Runtime, O(1) Space solution
def repeatedNTimes(A:[int]) -> int:
    if len(A) == 4 and A[0] == A[len(A)-1]: return A[0]
    for i in range(int(len(A)/2 + 2)):
        for k in range(1, 4):
            try:
                if A[i] == A[i+k]:return A[i]
            except:continue


if __name__ == "__main__":
    print(repeatedNTimes([40,553,6212,6212,6212,5447,6212,5359,6212,3878,6212,4052,2287,
                          6212,6212,6212,6212,6212,5716,2298,6212,6212,1290,6212,8245,
                          9243,4913,2149,6212,6212,6212,5687,8818,6212,9863,6212,6212,
                          3298,6212,6212,7006,6212,18,914,1846,9108,6212,6212,6212,6212,
                          6212,6212,5873,783,8653,6212,6212,1363,6212,1819,7245,8811,6212,
                          6212,2860,6212,472,6212,3016,6212,1732,6212,6212,6212,6212,7494,
                          6212,6212,6212,5747,5501,6212,6223,6212,7019,2387,3331,1042,
                          5781,1888,6212,5973,529,6212,8654,4245,6043,2732,2855,2710,
                          8870,6212,6212,6212,1641,9530,6212,4430,6212,6212,4346,5015,
                          6212,1623,4304,6186,3753,6212,6212,8773,6518,3070,6212,7803,
                          6212,6212,6212,9573,7359,5327,6212,6212,7466,6212,6212,4867,
                          3052,6212,6212,702,6212,6212,6212,6212,6212,1531,6222,4064,
                          8794,6212,4548,7174,3733,4397,6388,6212,5045,6212,1187,6212,
                          6212,6212,6212,9939,313,9676,6212,3514,1951,6212,6212,3037,
                          6212,1613,9534,6212,6212,6212,6212,6212,6212,81,6212,6212,
                          6212,6212,6212,1448,636,4562,6212,8396,6212,6212,4166,7512,
                          6212,6212,1020,6212]))