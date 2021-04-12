class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        list_ = [i+1 for i in range(n)]
        index = 0
        sign = 1
        for value in range(k,0,-1):
            index += 1 
            v=value*sign
            list_[index] = list_[index-1]+v
            sign = sign *-1
            
        return list_    
        
