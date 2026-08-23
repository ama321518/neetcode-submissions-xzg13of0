class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #given two strings as input return output is a boolean
        #constraints- they are both lowercase,an edge case is if we have one lement in the  two strings they are both anagrams
        #claqrifying question i could ask-what if empty both no characters so i am going to go with return false 

        #approch we are gonna compare count of each to other so what ds would help with that ?hashmapssss
        #we create hashmaps for both we get count of both then compare threir counts also becauseee i have done this over and over again i know we do an edge case check of if both lengths of both are the same or not and return true or false

        if len(s)!= len(t):
            return False

        hashmap_s ={}
        hashmap_t ={}
        
        for char in s:
            hashmap_s[char] = hashmap_s.get(char,0)+ 1
        for char in t:
            hashmap_t[char] = hashmap_t.get(char,0)+ 1
        return  hashmap_s ==  hashmap_t


        