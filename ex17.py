#!/usr/bin/env python
#--coding:utf-8--
from sys import argv
from os.path import exists
script,from_file,to_file = argv
print "Copying from %s to %s"%(from_file,to_file)
#we could do these two on one line too,how?
#input = open(from_file)
#indata = input.read()
indata = open(from_file).read()    #把上面两句话写成一句

print "The input file is %d bytes long"%len(indata)    #文件的大小

print "Doex the output file exist?%r"%exists(to_file)    #判断to_file文件是否存在，如果存在返回true，不存在返回false
print "Ready,hit RETURN to continue,CTRL-C to abort."
raw_input()

output = open(to_file,'w')    #以写入的方式打开文件，如果该文件不存在，则新建一个。
output.write(indata)    #将读取出来的内容indata写入到打开的文件中

print "Alright,all done."

output.close()
#input.close()
