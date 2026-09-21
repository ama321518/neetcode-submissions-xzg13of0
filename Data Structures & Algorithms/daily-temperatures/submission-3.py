class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack,list,store into pop ,get diff and store in list,retuen the days waiting list 
        result = len(temperatures) * [0]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                warmer = stack.pop()

                result[warmer] = i - warmer
            stack.append(i)

        return result

                
        