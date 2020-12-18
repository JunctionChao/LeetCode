#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-05
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

"""
get the next bigger number using the same digits of a number
ex: 123 -> 132
"""

def next_bigger(number):
    # 将数字转化为list
    number_to_list = []
    while number:
        number, mod = divmod(number, 10)
        number_to_list.append(mod)
    number_to_list = number_to_list[::-1]

    # 先找到右边比左边大的第一个位置
    size = len(number_to_list)
    for x in range(size-1, -1, -1):
        if number_to_list[x-1] < number_to_list[x]:
            break

    if x > 0:
        # 找第二层较大的数
        for y in range(size-1, -1, -1):
            if number_to_list[x-1] < number_to_list[y]:
                number_to_list[x-1], number_to_list[y] = \
                number_to_list[y], number_to_list[x-1]
                break
        # 后续的数是降序的，做置换调整
        for z in range((size-x)//2):
            number_to_list[x+z], number_to_list[size-z-1] = number_to_list[size-z-1], number_to_list[x+z]

        # 恢复为数字
        res, ex = 0, 0
        while number_to_list:
            res += number_to_list.pop() * 10**ex
            ex += 1
        return res

    # x==0说明左边的数字总是比右边的大
    else:
        return "the bigger number is not exist"


if __name__ == '__main__':
    print(next_bigger(4321))
    print(next_bigger(1342))
    print(next_bigger(1243))

