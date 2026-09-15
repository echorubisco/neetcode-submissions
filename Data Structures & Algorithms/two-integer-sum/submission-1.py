class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        for j in range(len(nums)):
            v = target - nums[j]
            if v in dict:
                idx = dict[v]
                if idx == j:
                    continue
                elif idx < j:
                    return [idx,j]
                else:
                    return [j,idx]
        
