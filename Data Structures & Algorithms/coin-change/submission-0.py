class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        self.memo = {i: -1000 for i in range(amount + 1)}

        def dp(coins, amount):
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1

            if self.memo[amount] != -1000:
                    return self.memo[amount]

            #initiate a big starting value
            res = float("inf")

            for coin in coins:
                
                subproblem = dp(coins, amount - coin)

                if subproblem == -1:
                    continue
                
                res = min(res, 1 + subproblem)

            self.memo[amount] = res if res != float('inf') else -1
            return self.memo[amount]

        return dp(coins, amount)