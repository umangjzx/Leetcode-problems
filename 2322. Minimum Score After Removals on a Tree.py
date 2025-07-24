from typing import List
import sys

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        sys.setrecursionlimit(10**6)
        n = len(nums)

        # Build tree
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        all_xor = 0
        for v in nums:
            all_xor ^= v

        parent = [-1] * n
        subxor = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u: int, p: int) -> int:
            nonlocal timer
            parent[u] = p
            timer += 1
            tin[u] = timer
            x = nums[u]
            for v in g[u]:
                if v == p:
                    continue
                x ^= dfs(v, u)
            subxor[u] = x
            tout[u] = timer
            return x

        dfs(0, -1)

        def is_ancestor(a: int, b: int) -> bool:
            return tin[a] <= tin[b] <= tout[a]

        ans = float('inf')

        # Nodes 1..n-1 correspond to the "child side" of each edge to parent[u]
        for u in range(1, n):
            for v in range(u + 1, n):
                if is_ancestor(u, v):
                    x1 = subxor[v]
                    x2 = subxor[u] ^ subxor[v]
                    x3 = all_xor ^ subxor[u]
                elif is_ancestor(v, u):
                    x1 = subxor[u]
                    x2 = subxor[v] ^ subxor[u]
                    x3 = all_xor ^ subxor[v]
                else:
                    x1 = subxor[u]
                    x2 = subxor[v]
                    x3 = all_xor ^ subxor[u] ^ subxor[v]

                diff = max(x1, x2, x3) - min(x1, x2, x3)
                if diff < ans:
                    ans = diff

        return ans
