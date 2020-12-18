#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-18
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/max-points-on-a-line/

# 这里用最大公约数GCD避免求斜率带来的浮点数比较问题
# 求最大公约数
def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a%b)

def maxPoints(points: list([list([int])])) -> int:
    if len(points) <= 2:
        return len(points)

    d = {}
    result = 0
    for i in range(len(points)):
        d.clear()
        overlap = 0 # 点重叠
        max_ = 0
        for j in range(i+1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx==0 and dy==0:
                overlap += 1
                continue
            gcd = get_gcd(dx, dy)
            if gcd:
                dx /= gcd
                dy /= gcd

            if dx in d:
                if dy in d[dx]:
                    d[dx][dy] += 1
                else:
                    d[dx][dy] = 1
            else:
                next_d = {}
                next_d[dy] = 1
                d[dx] = next_d

            max_ = max(max_, d[dx][dy])

        result = max(result, max_+overlap+1)

    return result


if __name__ == '__main__':
    print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4],[1,4]])) # 有重叠点

    print(maxPoints([[1,4],[1,1],[3,2],[5,3],[4,1],[2,3]]))