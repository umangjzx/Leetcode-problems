from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        left_sum = [0] * len(nums)
        max_heap = []
        current_left = 0
        
        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])  
            current_left += nums[i]
            if len(max_heap) > n:
                current_left += heapq.heappop(max_heap) 
            if len(max_heap) == n:
                left_sum[i] = current_left
        
        right_sum = [0] * len(nums)
        min_heap = []
        current_right = 0
        
        for i in range(len(nums) - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])  # use min-heap
            current_right += nums[i]
            if len(min_heap) > n:
                current_right -= heapq.heappop(min_heap)
            if len(min_heap) == n:
                right_sum[i] = current_right
        
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            diff = left_sum[i] - right_sum[i + 1]
            min_diff = min(min_diff, diff)
        
        return min_diff
