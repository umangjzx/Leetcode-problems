from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        m = len(conflictingPairs)
        # bucket by left endpoint
        buckets = [[] for _ in range(n + 2)]
        for i, (a, b) in enumerate(conflictingPairs):
            l, r = (a, b) if a < b else (b, a)
            buckets[l].append((r, i))

        INF = n + 1
        bestR = [INF] * (n + 2)     
        secondR = [INF] * (n + 2)   
        winner = [-1] * (n + 2)     

        min1R, min1Idx = INF, -1
        min2R, min2Idx = INF, -1

        for l in range(n, 0, -1):
            for r, idx in buckets[l]:
                if r < min1R or (r == min1R and idx < min1Idx):
                    if idx != min1Idx:
                        min2R, min2Idx = min1R, min1Idx
                    min1R, min1Idx = r, idx
                elif r < min2R or (r == min2R and idx < min2Idx):
                    min2R, min2Idx = r, idx

            bestR[l] = min1R
            secondR[l] = min2R
            winner[l] = min1Idx

        base = 0
        delta = [0] * m  
        for l in range(1, n + 1):
            old_bound = n if bestR[l] == INF else bestR[l] - 1
            base += old_bound - l + 1
            w = winner[l]
            if w != -1:
                new_bound = n if secondR[l] == INF else secondR[l] - 1
                inc = new_bound - old_bound
                if inc > 0:
                    delta[w] += inc

        best_gain = max(delta) if m else 0
        return base + best_gain
