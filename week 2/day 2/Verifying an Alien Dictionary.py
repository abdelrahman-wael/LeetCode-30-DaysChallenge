class Solution:
    def check(self,word1,word2,dic):
        minLen = min(len(word1),len(word2))
        for i in range(minLen):
            if dic[word1[i]] > dic[word2[i]]:
                return False
            elif dic[word1[i]] < dic[word2[i]] :
                return True
        return len(word1) <= len(word2)
                
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {order[i]:i for i in range(len(order))}
        for i in range(len(words)-1):
            if not self.check(words[i],words[i+1],dic):
                return False
                
        return True
        
