import json
f=open("D:\倒生树\书\A赫尔曼黑塞训练集\\train.json", 'r', encoding='utf8')
lines = json.load(f,strict=False)
for i in lines:
    print(len(i))
print(len(lines))
f.close()
print()