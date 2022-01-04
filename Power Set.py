def Solution(myset):
    res = myset.copy()
    for i in range(len(myset)):
        for j in range(i + 1, len(myset)):
            res.append(myset[i] + myset[j])
            print(res)


def Solution2(myset, i):
    subsets = []
    if i == len(myset):
        subsets = []
    else:
        subsets = Solution2(myset, i + 1)
        item = myset[i]
        moresubsets = []
        for subset in subsets:
            new = []
            new.append(subset)
            new.append(item)
            moresubsets.append(new)
        subsets.append(moresubsets)
    return subsets


myset = ["apple", "banana", "cherry"]

print(Solution2(myset, 0))
