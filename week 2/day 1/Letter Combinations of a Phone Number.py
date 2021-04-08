class Solution:  
    def conquer(self,firstHalf,secondHalf,dic):
        merged = []
        print(firstHalf)
        print(secondHalf)
        for subString1 in firstHalf:
            for subString2 in secondHalf:
                merged.append(subString1+subString2)
                
        return merged  
        
    def divideAndConquer(self,digits,dic):
        len_ = len(digits)
        if len_==1:
            return  [char for char in dic[digits[0]]]
        if len_>=2:
            mid = len_//2
            firstHalf=self.divideAndConquer(digits[:mid],dic)
            secondHalf=self.divideAndConquer(digits[mid:],dic)
        return self.conquer(firstHalf,secondHalf,dic)
            
            
        
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", '4':"ghi" ,'5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv","9":"wxyz" }
        if digits =="":
            return ""
        return self.divideAndConquer(digits,dic)
                
