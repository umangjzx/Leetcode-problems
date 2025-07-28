class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        count = 0

        # Step 1: Compute the maximum possible OR value
        for num in nums:
            max_or |= num

        # Step 2: Backtrack over all subsets
        def dfs(index: int, curr_or: int):
            nonlocal count
            if index == n:
                if curr_or == max_or:
                    count += 1
                return
            # Include nums[index]
            dfs(index + 1, curr_or | nums[index])
            # Exclude nums[index]
            dfs(index + 1, curr_or)

        dfs(0, 0)
        return count
