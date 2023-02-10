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


class Solution:

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


Solution()()

"""
整除
python for range前闭后开、切片也是前闭后开
"""
