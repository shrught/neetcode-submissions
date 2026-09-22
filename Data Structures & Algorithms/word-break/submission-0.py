class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}

        def dfs(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i : i + len(word)] == word and (i + len(word) <= len(s)):
                    
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return memo[i]

        return dfs(0)
