class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        timeSeries.sort(reverse=True)
        sum = duration
        lastTime = timeSeries[0]
        for time in timeSeries[1:]:
            sum += min(duration,lastTime-time)
            lastTime = time
        return sum