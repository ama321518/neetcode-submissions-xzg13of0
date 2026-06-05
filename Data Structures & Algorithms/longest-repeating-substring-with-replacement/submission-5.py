class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_c = 0

        best = 0

        hashmap = {}

        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1

            max_c = max(max_c, hashmap[s[end]])
            
            while (end-start + 1) - max_c > k:
                hashmap[s[start]]-= 1
                start += 1

            best = max(best, end - start + 1)
        return best




























  
























        