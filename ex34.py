#!/usr/bin/env python
#coding:utf-8

ordinal=raw_input("please input the ordinal number:")

animals = ['bear','python','peacock','kangaroo','whale','platpus']

i = int(ordinal)-1

print "The animal at %s is %s,and its number is %d."%(ordinal,animals[i],i)
print animals
