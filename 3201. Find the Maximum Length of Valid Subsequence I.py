from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        parities = [num % 2 for num in nums]
        max_length = 0
        for first_parity in [0, 1]:
            for second_parity in [0, 1]:
                if first_parity == second_parity:
                    count = sum(1 for p in parities if p == first_parity)
                    max_length = max(max_length, count)
                else:
                    count = 0
                    expected = first_parity
                    for p in parities:
                        if p == expected:
                            count += 1
                            expected = 1 - expected  # toggle
                    max_length = max(max_length, count)

        return max_length
