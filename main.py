#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'change many pictures name'

import sys
import os
from filetype import read_type

listinfo = input('请输入文件夹位置：')
picname = input('请输入文件头：')
mytype = input('请输入需要修改的类型(小写）：')
mylist = os.listdir(listinfo)
n = 1

#遇到同名文件时会报错，待解决
for filename in mylist:
	if mytype == '':
		os.rename(listinfo+'\\'+filename,listinfo+'\\'+picname+str(n)+'.'+read_type(filename))
		n += 1
	elif read_type(filename) == mytype:
		os.rename(listinfo+'\\'+filename,listinfo+'\\'+picname+str(n)+'.'+read_type(filename))
		n += 1
	else:
		pass

print('文件重命名成功！')
