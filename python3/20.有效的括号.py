#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = ["?"]
        d = {"(": ")", "[": "]", "{": "}", "?": "?"}
        for i in s:
            if i in d:
                stack.append(i)
            elif d[stack.pop()] != i:
                return False

        return len(stack) == 1


# @lc code=end
