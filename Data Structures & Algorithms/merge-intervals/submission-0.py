class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()#python automatikally sorts by first number
        #or intervals.sort(key= lambda x: x[0])sort by first number

        result = [intervals[0]]#result to store merged intervals

        for i in range(1,len(intervals)):
            if intervals[i][0] <= result[-1][1]:#remember idea of [1,3 in result and[2,6] being kompared against and we see it in,-1 is last otem and one is sekond item in list]
                result[-1][1] = max(result[-1][1], intervals[i][1])#when they overlap we update end of the last interval in result
            else:
                result.append(intervals[i])
        return result

        