"""
1. 子串：小于等于原字符串长度，由原字符串中任意个连续字符组成的子序列；

2. 回文：关于中间字符对称的字符串，例如："ababa"（单核）、"abccba"（双核）；

3. 最长回文子串：回文子串中最长的子串。


https://leetcode.cn/problems/longest-palindromic-substring/


# 解题思路：

1.蛮力法
遍历所有子串，判断是否是回文串，返回最长的回文子串

2.中心扩展
一个回文子串有唯一中心，根据中心定位遍历所有可能的子串，判断是否回文并返回最长子串

3.动态规划

4.
"""


class Solution1:

    def __init__(self):
        self.data = "zcdsfsaaadaaabf"

    def longest_palindrome(self, s: str) -> str:
        longest_str = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                flag = True
                for k in range(i, i + (j - i) // 2 + 1):
                    if s[k] != s[j - (k - i)]:
                        flag = False
                if flag and len(longest_str) < j - i + 1:
                    longest_str = s[i:j + 1]
        return longest_str

    def __call__(self, *args, **kwargs):
        result = self.longest_palindrome(self.data) or None
        print(result, len(result))


Solution1()()

"""
整除
python for range前闭后开、切片也是前闭后开
"""


class Solution2:

    def __init__(self):
        self.data = "zcdsfsaaadaaabm"

    def longest_palindrome(self, s: str) -> str:
        # 1.分解子问题，写状态转移方程
        # 2.赋初值
        # 3.开dp
        # 4.找边界条件

        if not s:
            return ""

        start = 0 # 记录字符串起始位置
        max_length = 0 # 记录回文串最大长度
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        # 初始化 赋初值很重要
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                dp[i][i+2] = True
                max_length = 2

        # 以字符串长度为1和2的子串为基础，推导长度：3~len 的子串的dp
        for i in range(3, len(s)):
            # // 从头开始，遍历长度为i的子串，并判断它们是否为回文串
            for j in range(len(s) - i):
                k = j + i - 1
                if dp[j+1][k-1] == True and s[j] == s[k]:
                    dp[j][k] = True
                    max_length = i
                    start = i

        return s[start:start+max_length]

    def __call__(self, *args, **kwargs):
        result = self.longest_palindrome(self.data) or None
        print(result, len(result))


Solution2()()
