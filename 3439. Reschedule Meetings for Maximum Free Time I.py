class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        gaps = [startTime[0]]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])
        
        window_size = k + 1
        current_sum = sum(gaps[:window_size])
        max_free = current_sum
        
        for i in range(window_size, len(gaps)):
            current_sum += gaps[i] - gaps[i - window_size]
            max_free = max(max_free, current_sum)
        
        return max_free
