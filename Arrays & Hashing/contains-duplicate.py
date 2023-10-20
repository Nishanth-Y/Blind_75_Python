class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,6,3,0,4]))