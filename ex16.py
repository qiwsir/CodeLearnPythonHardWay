#!/usr/bin/env python
#--coding:utf-8--
from sys import argv
script,filename = argv
print "We're going to erase %r."%filename
print "If you don't want that,hit CTRL-C."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,"w+")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ase you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."
target.close

print "please tell me the name of file again:"   #如果要打印本文档，在open的时候，必须使用参数"r" 
new_filename = raw_input(">")
txt = open(new_filename,"r")

print "Here's your file %r:"%filename
content = txt.read()
print content
#for line in content:
#    print line
txt.close()
