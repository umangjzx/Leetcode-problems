class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for num in arr:
            cur = {num | prev for prev in cur} | {num}
            res |= cur

        return len(res)
