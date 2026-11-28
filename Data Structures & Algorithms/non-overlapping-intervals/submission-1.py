class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])#take x and give back the last item[2,3]- take 3,key just means sort using this answer for each item)
        removed = 0
        last_end = float("-inf") #the very first end to compare against ,we know any start is bigger than this negative number ,so the first interval always gets kept.

        for start, end in intervals:#2 conditions
            if start >= last_end:
                last_end = end
            else:
                removed += 1
        return removed
            



        