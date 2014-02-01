#coding:utf-8
#from sys import argv    #sys，modules:模组，模块或者库，用import导入
import sys

#script,first,second,third = argv
script,first,second,third = sys.argv    #sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径；比如输入“python text.py beta”，那么sys.argv[0]就代表"test.py",sys.argv[1]为beta

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your thisr variable is:",third

print sys.argv[0]    #例如命令行中输入python ex13.py first second third,sys.argv[0]=ex13.py
print sys.argv[1]    #first
print sys.argv[2]    #second
print sys.argv[3]    #third
