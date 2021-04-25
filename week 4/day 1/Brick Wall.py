class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        columns=sum(wall[0])-1
        dic = {}
        if columns ==0 :
            return len(wall)
        rows = len(wall)
        
        maxEdges = 0
        for row in range(rows):
            for sum_ in accumulate(wall[row][:-1]):
                if sum_ in dic:
                    dic[sum_]+=1
                else:
                    dic[sum_] = 1
                maxEdges=max(dic[sum_],maxEdges)
                

            
        return  len(wall) - maxEdges
            