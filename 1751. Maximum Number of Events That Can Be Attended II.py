from typing import List
import bisect
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start day
        events.sort()
        
        # List of start days, for binary search
        start_days = [start for start, end, val in events]
        
        @lru_cache(None)
        def dp(i: int, remaining: int) -> int:
            # Base case: no events or no quota left
            if i == len(events) or remaining == 0:
                return 0
            
            # Skip current event
            skip = dp(i + 1, remaining)
            
            # Take current event
            _, end, value = events[i]
            
            # Find the next non-overlapping event
            next_i = bisect.bisect_right(start_days, end)
            take = value + dp(next_i, remaining - 1)
            
            return max(skip, take)
        
        return dp(0, k)
