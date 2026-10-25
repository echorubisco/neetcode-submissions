class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        sum = 0
        res = []
        def backtrack(nums,sum,path):
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[i:],sum+nums[i],path)
                path.pop()
        backtrack(nums,sum,path)
        return res

        
            