class Solution(object):
    def backspaceCompare(self, s, t):
        def build(s):
            stack = []

            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return stack

        return build(s) == build(t)
        