str1 = u"\u6000"#某个汉字的unicode码
print(str1)
print(str1.encode('utf-8').decode('unicode_escape'))
str2="卖"
print(str2.encode('unicode_escape')) 