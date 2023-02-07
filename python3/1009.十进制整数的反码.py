#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 将n转换为二进制，然后将每一位取反，最后转换为十进制
        # 1. 将n转换为二进制
        bin_n = bin(n)[2:]  # 去掉前缀0b
        r_bin_n = []
        # 2. 将每一位取反
        for i in bin_n:
            if i == '0':
                r_bin_n.append('1')
            else:
                r_bin_n.append('0')
        r_bin_n = ''.join(r_bin_n)
        # 3. 将二进制转换为十进制
        int_r_bin_n = int(r_bin_n, 2)
        # 4. 返回十进制
        return int_r_bin_n

        # 直接可写为下行形式
        # return int(''.join(['1' if i == '0' else '0' for i in bin(n)[2:]]), 2)

        """
        还有一种解法，原码和反码相加为2**n-1，n为原码的长度
        result = 2**n-1-n
        n_bin=bin(n)
        return 2**len(n_bin[2:])-1-n
        """


# @lc code=end
