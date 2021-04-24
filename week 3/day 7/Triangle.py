class Solution:
    def rec(self,triangle,row,column,memo):
        if row>=len(triangle):
            return 0
        if memo[row][column] !=None:
            return memo[row][column]
        memo[row][column] =triangle[row][column]+min(self.rec(triangle,row+1,column,memo),self.rec(triangle,row+1,column+1,memo))
        return memo[row][column]
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[None]*len(row) for row in triangle]
        
        return self.rec(triangle,0,0,memo)