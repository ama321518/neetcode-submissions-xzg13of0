class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best_substring = 0

        left = 0

        for right in range(len(s)):
            while s[right] in seen: #while loop cuz there might be more after if used if would look at just one and stop
                 seen.remove(s[left])
                 left += 1
            seen.add(s[right])
            best_substring = max(best_substring, right - left + 1)
        return best_substring

        