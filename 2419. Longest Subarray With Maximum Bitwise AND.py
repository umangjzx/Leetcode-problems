class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_value = max(nums)
        max_count = 0
        current_count = 0

        for num in nums:
            if num == max_value:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count
