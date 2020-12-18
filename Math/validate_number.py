#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-18
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 构造确定型有限自动机DFA
def isNumber(s: str) -> bool:
    #define a DFA
    state = [{},
            {'blank': 1, 'sign': 2, 'digit': 3, '.':4 }, 
            {'digit': 3, '.': 4},
            {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
            {'digit': 5},
            {'digit': 5, 'e': 6, 'blank': 9},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8, 'blank': 9},
            {'blank': 9}]
    currentState = 1
    for c in s:
        if c in '0123456789':
            c = 'digit'
        elif c == ' ':
            c = 'blank'
        elif c in '+-':
            c = 'sign'
        # if c not in stat[curretState].keys()这里没必要取得key同样可以
        if c not in state[currentState]:
            return False
        currentState = state[currentState][c]

    if currentState not in [3, 5, 8, 9]:
        return False

    return True


if __name__ == '__main__':
    print(isNumber('4e-2'))
    print(isNumber('99e2.5'))
    print(isNumber(' 0.34'))
    print(isNumber('-1.4e2  '))