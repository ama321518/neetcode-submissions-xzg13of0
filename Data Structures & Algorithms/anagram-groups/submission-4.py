from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input= strings of word,output- sorted words arranged
    

        hashmap = defaultdict(list)
        for word in strs:
            signature = "".join(sorted(word))
            hashmap[signature].append(word)
        return list(hashmap.values())