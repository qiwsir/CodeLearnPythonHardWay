#!/bin/usr/env python
#coding:utf-8

cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

#cities['_find'] = find_city

#while True:
#    print "State? (ENTER to quit)"
#    state = raw_input(">")
#    if not state:break
    #city_found = cities['_find'](cities,state)
#    city_found = find_city(cities,state)    
#    print city_found

print "State?(ENTER TO QUIT)"
state = raw_input(">")

for i in cities:
    if state == i:
        print find_city(cities,state)
    else:
        break
