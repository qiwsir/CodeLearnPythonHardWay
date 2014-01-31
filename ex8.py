#--coding:utf-8--
formatter = "%r %r %r %r"  #将输出格式赋予变量
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)  #打印结果'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'。特别注意，如果字符串中包含了'符号，则打印出来将该字符串包在""双引号内。
