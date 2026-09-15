class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in dict:
                dict[s] = [strs[i]]
            else:
                dict[s].append(strs[i])
        return [v for v in dict.values()]
                