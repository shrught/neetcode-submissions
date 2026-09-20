class Solution:
    def countSubstrings(self, s: str) -> int:

        self.totalPal = 0


        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                self.totalPal += 1

        for i in range(len(s)):
            #i itself
            self.totalPal += 1
            expand(i, i + 1)
            expand(i - 1, i + 1)

        return self.totalPal