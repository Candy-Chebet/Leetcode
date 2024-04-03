#Efficient
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for l1, l2, in zip(word1, word2):
            res +=l1+l2
            
        diff = len(word1) - len(word2)
        if diff > 0:
            res += word1[-diff:]
        elif diff<0:
            res+=word2[diff:]
        return res
    
result = (Solution().mergeAlternately('hello', 'world'))
print (result)