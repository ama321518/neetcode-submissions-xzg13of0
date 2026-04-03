class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strs =[ate,eat,tea]
        #create hashmap ,get the sorted signature then add in the wordsthat match

        from collections import defaultdict

        hashmap = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)
        return list(hashmap.values())