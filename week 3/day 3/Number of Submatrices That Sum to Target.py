import numpy as np

class Solution:
    
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        results=np.zeros((rows,columns))
        # results=[[0]*columns for row in range(rows)]
        for row in range(rows):
            for column in range(1,columns):
                results[row][column] = results[row][column-1]+matrix[row][column]
        counter = 0
        for j in range(columns):
            for k in range(j, columns):
                res, csum = {0: 1}, 0
                for r in results:
                    csum += r[k] - (r[j-1] if j else 0)
                    if csum - target in res: counter += res[csum-target]
                    res[csum] = res[csum] + 1 if csum in res else 1
        return counter
