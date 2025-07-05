from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)  
        lucky = -1
        
        for num, freq in count.items():
            if num == freq:
                lucky = max(lucky, num)
        
        return lucky
