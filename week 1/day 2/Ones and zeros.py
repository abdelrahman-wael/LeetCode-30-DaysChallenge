class Solution:
       

 # solving the problem using all possible permutation will lead to tle
 # interestingly if we used np.zeros this will lead to tle 
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for i in range(n+1)] for d in range(m+1)]
        for str in strs:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
    
        return dp[m][n]       


