class Solution(object):
    def isValidBST(self, root):
        stack = []
        prev = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev is not None and curr.val <= prev:
                return False

            prev = curr.val
            curr = curr.right

        return True