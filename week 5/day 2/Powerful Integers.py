class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        dic = {}
        i=j=0
        if x == 1 and y==1:
            if bound >=2:
                return [2]
            else:
                return []
        xi=1
        while xi < bound :
            j=0
            yj=1
            while (xi+yj) <= bound :
                value =xi+yj 
                if value <= bound:
                    if not (value in dic):
                        dic[value] = 0
                if y == 1:
                    break
                yj*=y
                
            if x == 1:
                break
            xi*=x
        
        return dic.keys()