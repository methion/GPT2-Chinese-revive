import os
from chardet import detect
train_data=['C-长佩2021年榜单100本', 
'F-废文2021年榜单120本', 'M-木苏里',
'其他中文', '古文小说', '合并语料', 
'测试集', '翁贝托', '诡异中文', 
'诡异中文1', '赫尔曼黑塞']
choose=train_data[2]
indir=r"D:\倒生树\书\\1训练集\\"+choose

file_n=os.listdir(indir)
# print(file_n)
outdir=r"D:\倒生树\书\\1训练集\processed\\"
procdir=outdir+choose+"\\"
if not os.path.exists(outdir + choose):
            os.mkdir(outdir + choose)


filedir = indir

fns = file_n
err=[]
for fn in fns:
    with open(indir+"\\"+fn, 'rb+') as fp:
        content = fp.read()
        if len(content)==0:
            continue
        else:
            codeType = detect(content)['encoding']
            if codeType is None:
                err.append(fn)
                codeType="utf-8"
            content = content.decode(encoding=codeType,errors= "ignore").encode("utf8")
            with open(procdir+"\\"+fn,"wb+") as fo:
                fo.write(content)
            print(fn, "：已修改为utf8编码")
            
print(err)