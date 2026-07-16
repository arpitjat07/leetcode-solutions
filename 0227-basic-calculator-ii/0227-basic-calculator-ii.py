class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = '+'
        stack = []

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                sign = ch
                num = 0

        return sum(stack)