class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        columns=len(obstacleGrid[0])
        rows = len(obstacleGrid)
        dp=[[0]*columns for i in range(rows)]
        print(dp)
        dp[rows-1][columns-1] = 1
        for row in reversed(range(rows)):
            for column in reversed(range(columns)):
                if( obstacleGrid[row][column] == 1 ):
                    dp[row][column] = 0
                else:
                    if row+1 < rows:
                        dp[row][column]+=dp[row+1][column]
                    if column+1 <columns:
                        dp[row][column]+=dp[row][column+1]
        return dp[0][0]