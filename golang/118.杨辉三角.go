/*
 * @lc app=leetcode.cn id=118 lang=golang
 *
 * [118] 杨辉三角
 */

// @lc code=start
func generate(numRows int) [][]int {
	res := make([][]int, numRows) // [[1],[1,1],[1,2,1],[1,3,3,1],[],...,[]]
	for i := range res {
		res[i] = make([]int, i+1)
		res[i][0] = 1
		res[i][i] = 1
		for j := 1; j < i; j++ {
			res[i][j] = res[i-1][j-1] + res[i-1][j]
		}
	}
	return res
}

// @lc code=end

