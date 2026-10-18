class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i,j = 0,0
        longest = 0
        length = 0
        while i < len(s) and j < len(s):
            if s[j] not in s[i:j]:
                j += 1
                length += 1
            else:
                while s[j] in s[i:j]:
                    i += 1
                length = j-i
            longest = max(longest, length)
        return longest


