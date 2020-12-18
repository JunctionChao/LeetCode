#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03
# @Author  : Yuanbo Zhao (chaojunction@gmail.com)
# @Link    : ${link}
# @Version : $Id$

def isPalindrome(x):
	if x<0 or (x%10==0 and x!=0):#排除负数和10的
		return False
	else:
		revertedNum = 0
		while x>revertedNum: #key point
			revertedNum = (revertedNum*10)+(x%10)
			x = x//10
		if x==revertedNum or x==revertedNum//10:
			return True
		else:
			return False
	# return x == int(str(x)[::-1]) if x >= 0 else False
if __name__ == '__main__':
	print(isPalindrome(0))