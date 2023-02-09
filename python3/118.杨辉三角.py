#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 递归
        if numRows == 0:
            return []
        # 递归终止条件
        if numRows == 1:
            return [[1]]
        # 递归公式
        res = self.generate(numRows - 1)
        res.append(
            [1] + [res[-1][i] + res[-1][i + 1] for i in range(numRows - 2)] + [1]
        )
        return res


# @lc code=end
