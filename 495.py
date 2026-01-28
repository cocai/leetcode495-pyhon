class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        timer = 0

        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration > timeSeries[i + 1]:
                timer += timeSeries[i + 1] - timeSeries[i]
            else:
                timer += duration
        
        return timer + duration