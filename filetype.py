#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'files type'

import sys
import os

filetype = ''

def read_type(filename):
	filename = filename.lower()
	if filename[-2] == '.':
		filetype = filename[-1]
	elif filename[-3] == '.':
		filetype = filename[-2:]
	elif filename[-4] == '.':
		filetype = filename[-3:]
	elif filename[-5] == '.':
		filetype = filename[-4:]
	else:
		print('请输入正确的文件名')
	return filetype

if __name__=='__main__':
	print(read_type('1.png'))
