#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-20
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def calculate(s: str) -> int:
    stack = []
    number, result, sign = 0, 0, 1

    for c in s:
        if c.isdigit():
            number = number * 10 + int(c)

        elif c == '+':
            result += sign * number
            number = 0
            sign = 1

        elif c == '-':
            result += sign * number
            number = 0
            sign = -1

        elif c == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1

        elif c == ')':
            result += sign * number
            number = 0
            result *= stack.pop()
            result += stack.pop()

    result += sign * number

    return result


if __name__ == '__main__':
    print(calculate(" 2-1 + 2 "))
    print(calculate("(1+(4+5+2)-3)+(6+8)"))