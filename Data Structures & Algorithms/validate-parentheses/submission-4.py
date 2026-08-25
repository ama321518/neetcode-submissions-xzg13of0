class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stack = []
        

        for char in s:
            if char in hashmap:#checjks closing bracket
                if stack and stack[-1] == hashmap[char]:#checks open bracket
                    stack.pop()#weve found a match
                else:
                    return False#empty or no match
            else:
                stack.append(char)#we saw an open bracket

        return not stack

            
                    




            #if char in mapping.values():
                #stack.append(char)

            #elif char in mapping:#if character is a closing bracket
                #if not stack or stack[-1] != mapping[char]#not empty -we saw a closing bracket,does the last open braxket not match the key in mapping
                #return False
                #stack.pop()
            #return not stack#returns true

    #mapping[char] is the value so the open bracket





    























        