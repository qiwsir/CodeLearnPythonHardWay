#!/usr/bin/env python
#--coding:utf-8--
#this one is like your scripts with argv
def print_two(*args):
    #arg1,arg2 = args
    #print "arg1:%r,arg2:%r"%(arg1,arg2)
    arg_length=len(args)
    for i in range(arg_length):    #range(a,b,c)代表从a开始（含a）到b（不含b），间隔是c（不含c）的整数。range(1,5)=>[1,2,3,4];range(1,5,2)=>[1,3];range(5)=>[0,1,2,3,4]
        print "arg[%d]:%r"%(i,args[i])   

# ok,that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r"%(arg1,arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1:%r"%arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed","Shaw","Kimmy","Tom")
print_two_again("zed","shaw")
print_one("first!")
print_none()
