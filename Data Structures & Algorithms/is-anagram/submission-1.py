class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()
        s1 = set(s)
        s2 = set(t)
        if len(s1) != len(s2):
            return False
        for char in s:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1
        for char in t:
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1
        return d1 == d2

        