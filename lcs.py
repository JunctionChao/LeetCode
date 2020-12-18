#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-04
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 最长公共子序列 LCS: Longest Common Subsequence

class LCS():
	def input(self, x, y):
		if type(x) != str or type(y) != str:
			print('input error')
			return None
		self.x = x
		self.y = y

	def compute_lcs(self):
		xlen = len(self.x)
		ylen = len(self.y)

		# 存储回溯方向的二维列表
		self.direction_list = [None] * xlen
		for i in range(xlen):
			self.direction_list[i] = [None] * ylen

		# 存储当前最长公共子序列长度的二维列表
		self.lcslen_list = [None] * (xlen + 1)
		for i in range(xlen + 1):
			self.lcslen_list[i] = [None] * (ylen + 1)

		# 空序列和任何序列的lcs都是空序列
		for i in range(xlen + 1):
			self.lcslen_list[i][0] = 0
		for j in range(ylen + 1):
			self.lcslen_list[0][j] = 0

		# 构建回溯方向表和LCS长度表
		for i in range(1, xlen + 1):
			for j in range(1, ylen + 1):
				if self.x[i-1] == self.y[j-1]:
					self.lcslen_list[i][j] = self.lcslen_list[i-1][j-1] + 1
					self.direction_list[i-1][j-1] = 0 # 左上
				else:
					if self.lcslen_list[i-1][j] > self.lcslen_list[i][j-1]:
						self.lcslen_list[i][j] = self.lcslen_list[i-1][j]
						self.direction_list[i-1][j-1] = 1 # 上
					elif self.lcslen_list[i-1][j] < self.lcslen_list[i][j-1]:
						self.lcslen_list[i][j] = self.lcslen_list[i][j-1]
						self.direction_list[i-1][j-1] = -1 # 左
					else: # self.lcslen_list[i-1][j] == self.lcslen_list[i][j-1]:
						self.lcslen_list[i][j] = self.lcslen_list[i-1][j]
						self.direction_list[i-1][j-1] = 2 # 左或上
		self.lcs_length = self.lcslen_list[-1][-1]
		# return self.direction_list, self.direction_list

	def print_lcs(self, curlen, i, j, s):
		if i == 0 or j == 0:
			return None

		if self.direction_list[i-1][j-1] == 0:
			if curlen == self.lcs_length:
				s += self.x[i-1]
				for i in range(len(s)-1, -1, -1):
					print(s[i])
				print('\n')
			elif curlen < self.lcs_length:
				s += self.x[i-1]
				self.print_lcs(curlen+1, i-1, j-1, s)
		elif self.direction_list[i-1][j-1] == 1:
			self.print_lcs(curlen, i-1, j, s)
		elif self.direction_list[i-1][j-1] == -1:
			self.print_lcs(curlen, i, j-1, s)
		else:
			self.print_lcs(curlen, i-1, j, s)
			self.print_lcs(curlen, i, j-1, s)

	def return_lcs(self):
		# 回溯入口
		self.print_lcs(1, len(self.x), len(self.y), '')


if __name__ == '__main__':
	lcs = LCS()
	x = 'safwrtbab'
	y = 'sftwryuaba'
	lcs.input(x, y)
	lcs.compute_lcs()
	lcs.return_lcs()