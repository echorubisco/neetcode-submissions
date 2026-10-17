class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for c in s:
            if (c-1) in s:
                continue
            length = 1
            while (c+length) in s:
                length += 1
            best = max(best,length)
        return best
            