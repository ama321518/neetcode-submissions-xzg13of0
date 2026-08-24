from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #input  is two strings and output is the largest string that divides both strings,a constraint they are uppercase cjarters ,a clarifying question i kould ask is why specifically is it uppercase i dont think it matter though
        #my approah firdt thing that comes to my mind is the way they do it in mathh so from math we import gcd then we 
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
        