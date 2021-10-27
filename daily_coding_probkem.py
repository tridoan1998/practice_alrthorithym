class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tempsum, arr = 0, []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(i + 2, len(nums)):
                    tempsum = nums[i] + nums[j] + nums[k]
                    if tempsum == 0:
                        arr.append([nums[i], nums[j], nums[k]])
        return arr
