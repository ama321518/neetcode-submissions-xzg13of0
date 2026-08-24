class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result =[]
        
        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char]
        
        for char in count:
            result.append(char * count[char])
        
        return ''.join(result)
        
        #learnt to use kount you just import from kolletions then you save it in variable then do kounter on the string so after kreate list then loop through order then if khar in kount append the khar times kount of kharater then delete then for remaining kharakters we just loop through kountered then append kharter times its kounttt