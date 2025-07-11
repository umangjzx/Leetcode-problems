import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort() 
        available = list(range(n)) 
        heapq.heapify(available)
        
        busy = []  
        count = [0] * n 

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                end_time, room = heapq.heappop(busy)
                delay = end - start 
                heapq.heappush(busy, (end_time + delay, room))
                end = end_time + delay

            count[room] += 1

        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
