/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
func maxArea(height []int) int {
	// 双指针
	left, right, res := 0, len(height)-1, 0
	// 从两边向中间靠拢
	for left < right {
		// go计算面积
		res = max(res, (right-left)*min(height[left], height[right]))
		// 每次移动较短的那个指针
		if height[left] < height[right] {
			// 因为移动较长的指针不会使得面积增大
			left++
		} else {
			right--
		}
	}
	return res
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end

