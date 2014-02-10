#!/usr/bin/env python
#coding:utf-8
"""
1、尽量少用while-loop，大部分时候for-loop是更好的选择。
2、重复检查你的while语句，确定你测试的布尔表达式最终会编程False.
3、如果不确定，就在while-loop的结尾打印出你要测试的值。看看它的变化。
"""
"""
def number(i,j,k):    
    while i<j: 
        print "At the top i is %d"%i
        numbers.append(i)
        i = i+k
        print "Numbers now:",numbers
        print "At the bottom i is %d"%i
        #return numbers
  """     

#i = 0
numbers = range(0,10)

#while i<6:
#    print "At the top i is %d"%i
#    numbers.append(i)
#    i = i+1
#    print "Numbers now:",numbers
#    print "At the bottom i is %d"%i

#number(0,9,2)

for i in range(len(numbers)):
    print "At the top i is %d"%numbers[i]
    print "Numbers now:",numbers[:i+1]

print "The numbers:"
for num in numbers:
    print num
