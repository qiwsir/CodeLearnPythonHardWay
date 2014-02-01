#--coding:utf-8--
print "How old are you?",    #逗号，表示下面的一行和本行输出在同一行，或者说，本行不输出换行符，本行没有结束
age = raw_input()    #将输入的内容赋给age，得到的是字符串。
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(age,height,weight)
