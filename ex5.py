#--coding:utf-8--
my_name='Zed A.Shaw'
my_age=35 #not a lie
my_height=75 #inches
my_weight=180 #lbs
my_eyes='Blue'
my_teeth="White"
my_hair="Brown"
print "Let's talk about %s"% my_name
print "He's %d inches tall."% my_height
print "He's %d pounds heavy."%my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair"%(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee."%my_teeth
#this line is tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d."%(my_age,my_height,my_weight,my_age+my_height+my_weight)
print "'%r'是一个万能格式化字符"
print "my eyes is %r,and I is %r inches tall"% (my_eyes,my_height)  #打印结果：my eyes is 'Blue',and I is 75 inches tall  特别注意%r和%s的区别,%r对应的字符串用引号，%s的没有，整数都没有引号。
print "I have %r teeth and %s hair"%(my_teeth,my_hair)
print "He is %r pounds and %d inches tall."%(my_weight,my_height)
