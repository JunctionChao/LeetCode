#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-04
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

"""
给定一个字符串，从中找出不含重复字符的最长子串的长度。
例如，"abcabcbb"的不含重复字母的最长子串为"abc"，其长度是3。"bbbbb"的最长子串是"b"，长度为1。

解题思路：
“滑动窗口法”

变量start和end分别记录子串的起点和终点

从左向右逐字符遍历原始字符串，每次将end + 1

字典countDict存储当前子串中各字符的个数

当新增字符c的计数 > 1时，向右移动起点start，并将s[start]在字典中的计数 - 1，直到countDict[c]不大于1为止

更新最大长度
"""

def lengthOfLongestSubstring(s):
    ans, start, end = 0, 0, 0
    countDict = dict()
    for c in s:
        end += 1
        countDict[c] = countDict.get(c, 0) + 1
        while countDict[c] > 1:
            countDict[s[start]] -= 1
            start += 1
        ans = max(ans, end - start)

    return ans

if __name__ == '__main__':
    s = 'acbbrthnuiit'
    print(lengthOfLongestSubstring(s))