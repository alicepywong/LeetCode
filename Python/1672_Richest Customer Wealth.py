class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Constraint
        if len(accounts) < 1:
            return
        for i in range(len(accounts)):
            if len(accounts[i]) > 50:
                return
            for j in range(len(accounts[i])):
                if accounts[i][j] < 1 or accounts[i][j] > 100:
                    return

        max_wealth = 0
        for i in range(len(accounts)):
            val = sum(accounts[i])
            max_wealth = max(max_wealth, val)

        return max_wealth
