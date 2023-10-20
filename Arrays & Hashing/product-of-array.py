class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)

        prefixValue = 1
        for i in range(len(nums)):
            res[i] = prefixValue
            prefixValue *= nums[i]
        postfixValue = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfixValue
            postfixValue *= nums[i]

        return res