class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in sSet:
                sSet.remove(s[l])
                l += 1
            sSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

        