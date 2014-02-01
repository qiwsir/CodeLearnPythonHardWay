#coding:utf-8
from sys import argv
name = raw_input("Tell me your name:")

print name,"said:"
for text in argv:
    print text

