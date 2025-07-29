from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        prev_ors = []
        max_or = 0

        for i in range(n - 1, -1, -1):
            current_ors = [(nums[i], 1)]
            for or_value, length in prev_ors:
                new_or = or_value | nums[i]
                if new_or != current_ors[-1][0]:
                    current_ors.append((new_or, length + 1))
            max_or = max(max_or, current_ors[-1][0])
            for or_value, length in current_ors:
                if or_value == max_or:
                    answer[i] = length
                    break
            prev_ors = current_ors

        return answer
if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestSubarrays([1, 0, 2, 1, 3]))  
    print(sol.smallestSubarrays([1, 2]))          