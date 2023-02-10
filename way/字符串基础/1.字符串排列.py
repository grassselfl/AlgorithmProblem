"""
题目：输入一个字符串，输出该字符串中字符的所有组合

例子：
输入：abc，组合：a、b、c、ab、ac、bc、abc

输入：aa，组合：a、aa


1. 题目
给定一个字符串，找出有该字符串所有字符排列组成的所有字符串。

2. 方法
迭代，遍历字符串，取遍历的字符当作首字符，对剩下的字符组成的字符串再次进行全排列操作。

注意：有可能出现相同字符的情况，用visited来记录首位置出现过的字符。
"""

# 回溯方法
class String:
    @staticmethod
    def data():
        return "abcdefghij"

    def xxx(self, data: str) -> list:
        if not data:
            return []
        elif len(data) == 1:
            return [data[0]]
        res = []
        visited = set()
        for i, item in enumerate(data):
            if item in visited:
                continue
            visited.add(item)
            new_s = data[:i] + data[i + 1:]
            tmp = self.xxx(new_s)
            for V in tmp:
                res.append(data[i] + V)
        return res


    def __call__(self, *args, **kwargs):
        print(self.xxx(self.data()))


String()()
