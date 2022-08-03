class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Constraints
        if num < 0 or num > 10**6:
            return

        cnt = 0
        while num > 0:
            if (num % 2) == 0:
                num /= 2
            else:
                num -= 1
            cnt = cnt + 1

        return cnt
