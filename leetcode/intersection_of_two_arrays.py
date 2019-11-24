#LEETCODE: 349. Intersection of Two Arrays

#First Variant: 48ms beats 87% of all submissions using straightforward approach
def intersection(self, nums1, nums2) -> [int]:
    res = []
    s = set(nums1)

    for e in nums2:
        if e in s:
            res.append(e)
            s.remove(e)
    return res


#Second Variant: 44ms beats 94% of all submissions using pythons built-in intersection operator for sets
def intersectionII(self, nums1, nums2) -> [int]:
    set1, set2 = set(nums1), set(nums2)

    return (set1 & set2)

#Third Vriant: Assuming lists are sorted -> a O(n) Runtime and O(1) Space Complexity approach (res not taken into consideration)
#48ms beats 87% of all submissions
def intersectionIII(nums1, nums2) -> [int]:
    if not nums1 or not nums2: return set()
    nums1, nums2 = sorted(nums1), sorted(nums2)
    idx1, idx2 = 0, 0
    p1, p2 = nums1[idx1], nums2[idx2]
    res = set()

    while True:
        if p1 == p2:
            res.add(p1)
            idx1 += 1
            idx2 += 1
            try:
                p1 = nums1[idx1]
                p2 = nums2[idx2]
            except:
                return res
        elif p1 < p2:
            idx1 += 1
            try:
                p1 = nums1[idx1]
            except:
                return res
        else:
            idx2 += 1
            try:
                p2 = nums2[idx2]
            except:
                return res


if __name__ == "__main__":
    intersectionIII([1,2,3],[1,2,2,3])
