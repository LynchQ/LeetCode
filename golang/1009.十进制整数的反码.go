/*
 * @lc app=leetcode.cn id=1009 lang=golang
 *
 * [1009] 十进制整数的反码
 */

// @lc code=start
func bitwiseComplement(n int) int {
	highBit := 1
	for i := 1; i <= 30; i++ {
		if n < 1<<i {
			break
		}
		highBit = i
	}
	mask := 1<<(highBit+1) - 1
	return n ^ mask
}

// @lc code=end

