class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
    
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)#interval ends before new one starts
            elif interval[0] > newInterval[1]:
                result.append(newInterval)#if interval we are on starts afternew interval
                newInterval = interval
            else:#the parts where overlap
                newInterval[0] = min(newInterval[0], interval[0])#you want the earliest of the 2
                newInterval[1] = max(newInterval[1], interval[1])#the end you want the latest of the two
        
        result.append(newInterval)#our safety net :no matter how the loop ends ,whatever newinterval kurrenly holds (merged or not) gets added #like if theres a new interval that isnt triggered by any of the  conditions
        return result

            