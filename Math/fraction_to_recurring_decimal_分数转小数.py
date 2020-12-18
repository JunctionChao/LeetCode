#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-19
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    sl = list()
    sign = "-" if (numerator * denominator) < 0 else ""
    # sign = "-" if ((numerator > 0) ^ (denominator > 0)) else ""
    sl.append(sign)

    # integral part
    n, remainder = divmod(abs(numerator), abs(denominator))
    sl.append(str(n))
    if remainder == 0:
        return "".join(sl)

    # fractional part
    sl.append(".")
    d = dict()
    d[remainder] = len(sl)
    while remainder != 0:
        remainder *= 10
        n, remainder = divmod(remainder, abs(denominator))
        sl.append(str(n))
        if remainder in d:
            index = d[remainder]
            sl.insert(index, "(")
            sl.append(")")
            break

        else:
            d[remainder] = len(sl)

    return "".join(sl)


if __name__ == '__main__':
    print(fractionToDecimal(11, 100))
    print(fractionToDecimal(2, 3))