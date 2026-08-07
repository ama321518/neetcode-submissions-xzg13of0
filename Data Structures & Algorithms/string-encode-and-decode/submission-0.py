class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "@" + s
        return result

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            delimeter = s.index("@", i)
            length = int(s[i:delimeter])
            word = s[delimeter + 1 : delimeter + 1 + length]
            res.append(word)
            i = delimeter + 1 +length
        return res


        

  

            #we have the structure now


                
               
