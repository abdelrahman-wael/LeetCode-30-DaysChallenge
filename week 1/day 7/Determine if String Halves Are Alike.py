class Solution:
    
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        mid =len(s)//2
        equal = 0
        for i in range(mid):
            if s[i] in vowels:
                equal += 1
            if s[i+mid] in vowels:
                equal -=1
        return equal == 0
