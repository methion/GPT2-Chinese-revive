import os
import re
#input dir
train_data=["诡异中文","赫尔曼黑塞","其他中文","古文小说","翁贝托"]
choose=train_data[1]
indir=r"D:\倒生树\书\\1训练集\\"+choose

file_n=os.listdir(indir)
print(file_n)
outdir=r"D:\倒生树\书\\1训练集\processed\\"
procdir=outdir+choose+"\\"
if not os.path.exists(outdir + choose):
            os.mkdir(outdir + choose)
# f2=open(outdir,"w",encoding="utf-8")
# f2.write("[")

#遍历文件
for fi in file_n:
    filepath=indir+"\\"+fi
    print(fi)
    #f=open("D:\倒生树\书\A赫尔曼黑塞训练集\给所有人的黑塞童话.txt", "r",encoding="utf-8")
    with open(filepath, "r", encoding="utf-8-sig") as f1:
        rlines=f1.readlines()
        for n in range(len(rlines)):
            line=rlines[n]
            mline=re.match("^[^“”！？。，……\s]{1,8}\n$",line)
            if mline!=None:
                print(line)
                rlines[n]=""

        # print(f'正在导入  {i}')
        # content=f1.read()
        rlines=list(filter(None,rlines)) 
        content="".join(rlines)
        content.strip()
        # 去除非法字符
        content=content.replace("本书由“ePUBw.COM”整理ePUBw.COM 提供最新最全的优质电子书下载","")
        content = content.replace("\u200b", "")
        content = content.replace("\u3000", "")
        # content = content.replace("☆、", "")  
        content = content.replace("\\","")
        #分割
        tail=len(content)
        clist=[]
        if tail>50000:
            i=0
            for i in range(0,tail,40000):
                clist.append(content[i:i+40000])
                #不用担心边界溢出，如果到底了会自动添加最后一截不足4w的部分
                # 同时退出循环
            
        else:
            clist=[content]
            # clist=re.split("第.+卷.*\n|第.+部.*\n",content)
        #去空
        clist=list(filter(None,clist)) 

        #clist=re.split("目录\n|译本序\n",content)       
        #删除注释和xx章
        chapter="第.*章.*\n"
        annote="\[\d*\].*\n"
        enter="\n+"
        
        repl=''  
        for c in range(len(clist)):
            clist[c]=re.sub(enter, "\n", clist[c])
            clist[c]=re.sub(chapter, repl, clist[c])
            clist[c]=re.sub(annote,repl,clist[c])


    print("ok")
    with open(procdir+fi,"w",encoding="utf-8") as f2:
        for con in clist:
            f2.write(con)
        print("finish "+fi)
        