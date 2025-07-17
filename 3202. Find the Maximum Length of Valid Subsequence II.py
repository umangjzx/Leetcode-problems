from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                if mod in dp[j]:
                    dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                else:
                    dp[i][mod] = max(dp[i][mod], 2)  # start of a new valid subsequence
                max_len = max(max_len, dp[i][mod])
        
        return max_len
