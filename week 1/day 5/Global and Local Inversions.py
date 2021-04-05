class Solution:
    def valid(self,list_):
        count =0
        for i in range(len(list_)):
            value = list_[i]
            count = abs(i - value )
            
            if count > 1:
                return False
    
        return True
        
    def isIdealPermutation(self, A: List[int]) -> bool:
        
        if len(A) == 1:
            return True
        return self.valid(A) 
            
        
