from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [0] * (n + 1)
        if n > 0:
            gaps[0] = startTime[0]
            for i in range(1, n):
                gaps[i] = startTime[i] - endTime[i - 1]
            gaps[n] = eventTime - endTime[-1]
        else:
            return eventTime
        
        maxLeft = [0] * (n + 1)
        maxLeft[0] = gaps[0]
        for i in range(1, n + 1):
            maxLeft[i] = max(maxLeft[i - 1], gaps[i])
        
        maxRight = [0] * (n + 1)
        maxRight[n] = gaps[n]
        for i in range(n - 1, -1, -1):
            maxRight[i] = max(maxRight[i + 1], gaps[i])
        
        ans = 0
        for i in range(n):
            meeting_duration = endTime[i] - startTime[i]
            left_gap = gaps[i]
            right_gap = gaps[i + 1]
            merged_gap = left_gap + right_gap
            leftMax = maxLeft[i - 1] if i > 0 else 0
            rightMax = maxRight[i + 2] if i + 2 <= n else 0
            if meeting_duration <= max(leftMax, rightMax):
                ans = max(ans, merged_gap + meeting_duration)
            else:
                ans = max(ans, merged_gap)
        return ans
