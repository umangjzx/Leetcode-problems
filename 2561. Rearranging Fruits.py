from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total_freq = freq1 + freq2

        for fruit, count in total_freq.items():
            if count % 2 != 0:
                return -1

        extra1 = []
        extra2 = []
        for fruit in total_freq:
            diff = freq1[fruit] - freq2[fruit]
            if diff > 0:
                extra1.extend([fruit] * (diff // 2))
            elif diff < 0:
                extra2.extend([fruit] * (-diff // 2))

        extra1.sort()
        extra2.sort(reverse=True)

        min_elem = min(min(basket1), min(basket2))
        cost = 0

        for a, b in zip(extra1, extra2):
            cost += min(min(a, b), 2 * min_elem)

        return cost
