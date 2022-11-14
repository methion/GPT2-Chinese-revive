import json,os

wuzei="D:\倒生树\书\A其他中文训练集\乌贼\\"
heisai="D:\倒生树\书\A赫尔曼黑塞训练集\\"
wuzei_json="wuzei.json"
train="train.json"
ori="train.txt"
path=heisai
file_n=os.listdir(path)
if ori in file_n:
    os.rename(path+ori, path+train)
f=open(path+train, 'r', encoding='utf8')
lines = json.load(f,strict=False)
for i in lines:
    print(len(i))
print(len(lines))
f.close()
print()


