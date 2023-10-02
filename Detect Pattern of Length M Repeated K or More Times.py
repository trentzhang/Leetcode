class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        string = "".join([str(i) for i in arr])
        mSubStringWithKRepeatList = [string[i : i + m] for i in range(len(arr) - m + 1)]
        for pattern in mSubStringWithKRepeatList:
            if pattern * k in string:
                return True

        return False


print(Solution().containsPattern(arr, m, k))
