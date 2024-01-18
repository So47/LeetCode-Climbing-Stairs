class Solution:
    def climbStairs(self, n: int) -> int:
        # The base cases (0 and 1 steps) are initialized to 1 since there is only one way to reach them.
        if n == 0 or n == 1:
            return 1

        # # Create db table of size n+1 to store the number of ways to reach each step
        # dp = [0] * (n+1)

        # dp[0] = dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

# another solution reduces the space complexity from O(n) to O(1) while maintaining the time complexity at O(n)

        # Initialize the first two steps
        prev, current = 1, 1

        for i in range(2, n + 1):
            # Compute the number of ways to reach the current step
            temp = current
            current = prev + current
            prev = temp

        return current
    



        
