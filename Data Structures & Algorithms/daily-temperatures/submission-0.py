class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []#storing indexes

        result = [0] * len(temperatures)

        for i in range (len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                yesterday = stack.pop()
                result[yesterday]= i - yesterday
            stack.append(i)
        return result


