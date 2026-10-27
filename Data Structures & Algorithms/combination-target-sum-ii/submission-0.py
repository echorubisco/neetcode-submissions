class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path,res = [],[]
        def backtrack(i,path):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                else:
                    path.append(candidates[j])
                    backtrack(j+1,path)
                    path.pop()
        backtrack(0,path)
        return res