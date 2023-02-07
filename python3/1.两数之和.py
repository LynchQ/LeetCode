#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力法
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # 2. 两遍哈希表
        r: Dict[int, int] = {}
        for i, v in enumerate(nums):
            if target - v in r:
                return [r[target - v], i]
            r[v] = i

        return []


# @lc code=end
