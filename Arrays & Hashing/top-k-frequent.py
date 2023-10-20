from collections import Counter
class Solution:
    def topKFrequent(self, nums, k: int):
        freq = [[] for i in range(len(nums) + 1)]

        for key, item in Counter(nums).items():
            freq[item].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
