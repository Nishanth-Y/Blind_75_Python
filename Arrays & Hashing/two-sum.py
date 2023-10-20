class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {} 
        for i, n in enumerate(nums):
            difference = target - n
            if difference in Hmap:
                return [Hmap[difference], i]
            Hmap[n] = i
        return