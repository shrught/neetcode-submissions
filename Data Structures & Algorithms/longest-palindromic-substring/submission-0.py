class Solution:
    def longestPalindrome(self, s: str) -> str:
        resMap = {}

        for i in range(len(s)):
            oddLen, evenLen = 1, 0
            eleft, eright = i, i + 1
            oleft, oright = i - 1,  i + 1

            #calculate evenLen
            while eleft >= 0 and eright < len(s):
                if s[eleft] == s[eright]:
                    eleft -= 1
                    eright += 1
                    evenLen += 2
                else:
                    break
            
            #calculate oddLen
            while oleft >= 0 and oright < len(s):
                if s[oleft] == s[oright]:
                    oleft -= 1
                    oright += 1
                    oddLen += 2
                else:
                    break
            
            resMap[i] = s[oleft + 1 : oright] if oddLen >= evenLen else s[eleft + 1 : eright]


        maxRes = ""

        for i in resMap:
            if len(resMap[i]) > len(maxRes):
                maxRes = resMap[i]

        return maxRes
