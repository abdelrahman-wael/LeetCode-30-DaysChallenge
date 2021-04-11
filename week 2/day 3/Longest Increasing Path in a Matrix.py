class Solution:
    def validIndex(self,index,rows,columns):
        row,column = index
        if row < 0 or row >= rows:
            return False
        if column < 0 or column >= columns:
            return False
        return True
            
    def floodFill(self,index,matrix,visited,prev,rows,columns):
        row,column = index
        if not self.validIndex(index,rows,columns) or prev >= matrix[row][column]:
            return 0
        if visited[row][column]:
            return visited[row][column]
        path1 = self.floodFill((row+1,column),matrix,visited,matrix[row][column],rows,columns)
        path2 = self.floodFill((row-1,column),matrix,visited,matrix[row][column],rows,columns)
        path3 = self.floodFill((row,column+1),matrix,visited,matrix[row][column],rows,columns)
        path4 = self.floodFill((row,column-1),matrix,visited,matrix[row][column],rows,columns)
        visited[row][column] = 1 + max(path1,path2,path3,path4)
        return visited[row][column]
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        columns = len(matrix[0])
        visited = [[0]*columns for i in range(rows)]
        maxPath = -1
        for row in range(rows):
            for column in range(columns):
                maxPath=max(maxPath,self.floodFill((row,column),matrix,visited,-1,rows,columns))
        return maxPath
