class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        best = 0
        max_count = 0
        

        hashmap = {}

        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end],0) + 1
           
            max_count = max(max_count, hashmap[s[end]])

            while (end - start + 1)- max_count > k:#i know we reduee but its how 
                hashmap[s[start]] -= 1
                start += 1
            

            best = max(best, end - start + 1) #i think im wrong
        return best
            



























  
























        