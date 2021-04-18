class Solution:
    def rmDup(self,list_,array ,k):
        for i in range(len(array)):
            char = array[i]
            if not list_:
                list_.append([char,1])
                continue
            oldChar, charCounter=list_.pop()
            if char == oldChar:
                charCounter += 1
                if charCounter < k:
                    list_.append([oldChar,charCounter])
            else:
                list_.append([oldChar,charCounter])
                list_.append([char,1])
            
            
            
    def removeDuplicates(self, s: str, k: int) -> str:
        list_ =[]
        self.rmDup(list_,s,k)
        newS = ""
        for e in list_:
            newS += e[0]*e[1]
        return newS
        
