#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-20
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    overlap = max(min(C,G)-max(A,E), 0) * max(min(D,H)-max(B,F), 0)
    return (C-A)*(D-B) + (G-E)*(H-F) - overlap


if __name__ == '__main__':
    print(computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))