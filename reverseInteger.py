#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01
# @Author  : Yuanbo Zhao (chaojunction@gmail.com)
# reverse integer
'''
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

import os
def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	m = -1 if x < 0 else 1
	x = x*m

	n = 0
	while x > 0:
		n = (n * 10) + (x % 10) # clever
		x = x // 10

	if n > 0x7FFFFFFF:
		return 0

	return n*m
'''
def reverseInteger(x):
	units = []
	signed = -1 if x < 0 else 1
	num = x*signed
	if num < 10:
		return num
	
	while num >= 10:
		
		units.append(num%10)
		num = num // 10
		if num < 10:
			units.append(num)
	reverse = 0
	l = len(units)
	for i in range(l):
		reverse = reverse + units[i]*10**(l-1-i)
	if reverse > 0x7FFFFFFF:
		return 0
	reverse = reverse*signed

	return reverse
'''
if __name__ == '__main__':
	num = 236469
	# print(reverseInteger(num))
	print(reverse(num))