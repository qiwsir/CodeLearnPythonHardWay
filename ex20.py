#!/usr/bin/env python
#--coding:utf-8--

from sys import argv
script,input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)    #回到文件开始

def print_a_line(line_count,f):
    print line_count,f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)
print "now the cursor is:",current_file.tell()    #通过file.tell()查看当前位置

print "\nNow let's rewind, kind of like a tape."

rewind(current_file)   #经过20行的操作，current_file文件对象的指针已经到了该文件的最后，此步旨在让文件从开头开始。否则，在30、34、38的输出中，只有行号，没有内容。
print "now the cursor is:",current_file.tell()
print "\nLet's print three lines:"

current_line = 1
print_a_line(current_line,current_file)
print "now the cursor is:",current_file.tell()

current_line = current_line+1
print_a_line(current_line,current_file)
print "now the cursor is:",current_file.tell()

current_line = current_line+1
print_a_line(current_line,current_file)
print "now the cursor is:",current_file.tell()
