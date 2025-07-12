from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @lru_cache(None)
        def dfs(n, a, b):
            if a + b == n + 1:  # a and b meet
                return (1, 1)
            if a + b > n + 1:   # mirror to left half
                a, b = n + 1 - b, n + 1 - a
            
            min_round = float('inf')
            max_round = float('-inf')

            for i in range(1 << ((n - 1) // 2 + 1)):  # simulate each possible winner scenario
                nxt = []
                l, r = 1, n
                x = i
                while l < r:
                    if (l == a and r == b) or (l == b and r == a):  # meeting condition
                        break
                    if l == a or r == a:
                        nxt.append(a)
                    elif l == b or r == b:
                        nxt.append(b)
                    else:
                        nxt.append(l if x & 1 == 0 else r)
                        x >>= 1
                    l += 1
                    r -= 1
                else:
                    if l == r:  # middle player
                        nxt.append(l)

                    nxt.sort()
                    na = nxt.index(a) + 1
                    nb = nxt.index(b) + 1
                    eAr, lr = dfs(len(nxt), na, nb)
                    min_round = min(min_round, er + 1)
                    max_round = max(max_round, lr + 1)

            return (min_round, max_round)

        return list(dfs(n, firstPlayer, secondPlayer))
