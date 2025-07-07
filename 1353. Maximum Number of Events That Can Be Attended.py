import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_events = len(events)
        min_heap = []
        day = 0
        i = 0
        attended = 0

        while i < total_events or min_heap:
            if not min_heap:
                day = events[i][0]

            while i < total_events and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

            day += 1

        return attended
