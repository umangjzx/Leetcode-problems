from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # 1) compress consecutive duplicates
        a = [nums[0]]
        for x in nums[1:]:
            if x != a[-1]:
                a.append(x)
        cnt = 0
        for i in range(1, len(a) - 1):
            if (a[i-1] < a[i] > a[i+1]) or (a[i-1] > a[i] < a[i+1]):
                cnt += 1
        return cnt
