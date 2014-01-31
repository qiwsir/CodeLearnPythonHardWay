#--coding:utf-8--
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)
print x
print y

print "I said: %r." % x     #如果x是一个字符串，则对应%r自动带上引号，但是%s则无引号。
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious  #相当于下面语句
print "Isn't that joke so funny?! %r" % False

print "Isn't that joke so funny?! %r" % binary

w = "This is the left side of ..."
e = "a string with a right side."

print w+e
