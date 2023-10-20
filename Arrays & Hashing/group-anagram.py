from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for string in strs:
            count = [0]*26
            for character in string:
                count[ord(character) - ord('a')] += 1
            result[tuple(count)].append(string)

        return result.values()