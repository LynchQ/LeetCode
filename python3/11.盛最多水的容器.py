#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针
        max_area = 0
        # 左右指针
        left, right = 0, len(height) - 1
        # 左指针小于右指针
        while left < right:
            # 计算面积
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            # 移动指针
            if height[left] < height[right]:
                # 左指针小于右指针，移动左指针
                left += 1
            else:
                # 左指针大于右指针，移动右指针
                right -= 1
        # 返回最大面积
        return max_area


# @lc code=end
