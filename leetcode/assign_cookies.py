def findContentChildren(g: [int], s: [int]) -> int:
    g = sorted(g)
    s = sorted(s)
    i,j,res = 0,0,0

    while True:
        if i == len(g) or j == len(s): return res
        while s[j] < g[i]:
            j+=1
            if j == len(s): return res
        res+=1
        i+=1
        j+=1



if __name__ == '__main__':
    print(findContentChildren([1,2],[1,2,3]))
