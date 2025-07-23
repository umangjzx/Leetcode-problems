class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, score):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return total, "".join(stack)
        
        # Prioritize the higher scoring pair first
        if x >= y:
            score1, remaining = remove_pair(s, 'a', 'b', x)
            score2, _ = remove_pair(remaining, 'b', 'a', y)
        else:
            score1, remaining = remove_pair(s, 'b', 'a', y)
            score2, _ = remove_pair(remaining, 'a', 'b', x)
        
        return score1 + score2
