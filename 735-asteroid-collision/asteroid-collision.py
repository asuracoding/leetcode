class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        new_stack = []
        for num in asteroids:
            while new_stack and new_stack[-1] > 0 and num < 0:
                if abs(new_stack[-1]) == abs(num):
                    new_stack.pop()
                    break
                elif abs(new_stack[-1]) > abs(num):
                    break
                else:
                    new_stack.pop()
            else:
                new_stack.append(num)
        return new_stack