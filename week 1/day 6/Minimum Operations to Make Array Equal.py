class Solution:
# there is a more efficient solution where you can try to find a formula that predict the sum 
# of num of operation O(1)
    def minOperations(self, n: int) -> int:
        x= [(2*i) + 1 for i in range(n)]
        mean= sum(x)/len(x)
        numOperation = 0 
        for i in range(len(x)//2):          
            numOperation += mean - (i*2)+1
        
        return int(numOperation)
        
        
