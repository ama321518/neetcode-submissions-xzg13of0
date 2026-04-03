class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
#exampleAABA,k =1

        count = {}
        left = 0
        best = 0
        max_less_k = 0#lets us see count in a window

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) +1
            max_less_k = max(max_less_k,count[s[right]])
            
            if (right- left + 1) - max_less_k > k:
                count[s[left]]-=1
                left += 1
            best = max(best,right -left +1 )
        return best