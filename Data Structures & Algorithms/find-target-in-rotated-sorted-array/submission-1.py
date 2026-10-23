class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0,len(nums)
        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[-1]:
                if nums[mid] < target <= nums[-1]:
                    lo = mid+1
                else:
                    hi = mid
            else:
                if nums[-1] < target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid+1
        return -1