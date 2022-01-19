class Solution:
    def twoSum(self, nums, target):
        vals = []
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals.index(nums[i]), i]
            vals.append(target - nums[i])
        

a = Solution()
print(a.twoSum(nums = [2,7,11,15], target = 9))
        