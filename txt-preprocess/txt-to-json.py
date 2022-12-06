import os
import re

#input dir
indir="D:\倒生树\书\A诡异中文训练集"
#output dir
file_n=os.listdir(indir)
print(file_n)
outdir="D:\倒生树\书\A其他中文训练集\乌贼\\train.txt"
f2=open(outdir,"a",encoding="utf-8")
f2.write("[")
for filename in file_n:
    filepath=indir+"\\"+filename
    print(filename)
    flag=False
    if filename == file_n[-1]:
        flag=True
    with open(filepath, "r", encoding="utf-8-sig") as f1:
        
        content=f1.read()
        
        content.strip()

        
        # 去除\u200b字符
        content = content.replace("\u200b", "")
        content = content.replace("\u3000", "")
        content = content.replace("☆、", "")
        
        content = content.replace("\\","")
        tail=len(content)
        clist=[]
        #分割
        if tail>50000:
            i=0
            
            for i in range(0,tail,40000):
                clist.append(content[i:i+40000])
            clist.append(content[int(i):int(tail)])
        else:
            clist=re.split("第.+卷.*\n|第.+部.*\n",content)

        clist=list(filter(None,clist)) 
        #删除注释和xx章
        chapter="第.+卷.*\n|第.+章.*\n|第.+部.*\n"
        juan="【 卷.* 】"
        zjml="章节目录.*\n"#modu
        http="<strong>.*<strong>"#三天两觉
        duwo="※.*第"
        link="<a.*a>"
        zuozhe = "作者有话.*第"
        u="\\u[a-zA-Z0-9]{4}"
        # enter="(\n)+"
        repl=''

  
        
        
        for c in range(len(clist)):
            clist[c]=re.sub(link, repl, clist[c])
           
            # clist[c]=re.sub(enter, "\n", clist[c])
            if "默读" in filename:
                clist[c]=re.sub(zjml, repl, clist[c])
            if "三天两觉" in filename:
                clist[c]=re.sub(http, repl, clist[c])
            if "渡我" in filename:
                clist[c]=re.sub(duwo, "第", clist[c])

            clist[c]=re.sub(zuozhe, "第", clist[c])
            clist[c]=re.sub(chapter, repl, clist[c])
            if c==len(clist)-1 and flag:
                print("end")
                f2.write("\"{}\"".format(clist[c]))
            else:
                f2.write("\"{}\",".format(clist[c]))
            
    print("ok")
f2.write("]")
f2.close()

#region 乌贼
# #####################################
# #input dir
# indir="D:\倒生树\书\A其他中文训练集\乌贼"
# #output dir
# file_n=os.listdir(indir)
# print(file_n)
# outdir="D:\倒生树\书\A其他中文训练集\乌贼\\train.txt"
# f2=open(outdir,"a",encoding="utf-8")
# f2.write("[")
# for i in file_n:
#     filepath=indir+"\\"+i
#     print(i)
#     flag=False
#     if i == file_n[-1]:
#         flag=True
#     with open(filepath, "r", encoding="utf-8-sig") as f1:
        
#         # print(f'正在导入  {i}')
#         content=f1.read()
        
#         content.strip()
#         # 合并正文中过多的空格
        
#         # 去除\u200b字符
#         content = content.replace("\u200b", "")
#         content = content.replace("\u3000", "")
#         content = content.replace("\\","")
#         tail=len(content)
#         clist=[]
#         if tail>50000:
#             i=0
            
#             for i in range(0,tail,40000):
#                 clist.append(content[i:i+40000])
#             clist.append(content[int(i):int(tail)])
#         else:
#             clist=re.split("第.+卷.*\n|第.+部.*\n",content)

#         clist=list(filter(None,clist)) 
#         #删除注释和xx章
#         chapter="第.+卷.*\n|第.+章.*\n|第.+部.*\n"
#         link="http.*biqugexsw8\.?"
#         u="\\u[a-zA-Z0-9]{4}"
#         # enter="(\n)+"
#         repl=''

  
        
        
#         for c in range(len(clist)):
#             clist[c]=re.sub(link, repl, clist[c])
#             clist[c]=re.sub(chapter, repl, clist[c])
#             # clist[c]=re.sub(enter, "\n", clist[c])
            
#             if c==len(clist)-1 and flag:
#                 print("end")
#                 f2.write("\"{}\"".format(clist[c]))
#             else:
#                 f2.write("\"{}\",".format(clist[c]))
            
#     print("ok")
# f2.write("]")
# f2.close()

#endregion ####################################

#region #黑塞
############################################
# #input dir
# indir="D:\倒生树\书\A赫尔曼黑塞训练集"
# #output dir
# file_n=os.listdir(indir)
# print(file_n)
# outdir="D:\倒生树\书\A赫尔曼黑塞训练集\output.txt"
# f2=open(outdir,"a",encoding="utf-8")
# f2.write("[")

# for i in file_n:
#     filepath=indir+"\\"+i
#     print(i)
#     #f=open("D:\倒生树\书\A赫尔曼黑塞训练集\给所有人的黑塞童话.txt", "r",encoding="utf-8")
    
#     with open(filepath, "r", encoding="utf-8-sig") as f1:
        
#         # print(f'正在导入  {i}')
#         content=f1.read()
#         content.strip()
#         content=content.replace("本书由“ePUBw.COM”整理ePUBw.COM 提供最新最全的优质电子书下载\
# ","")
 
#         clist=re.split("目录\n|译本序\n",content)       
#         #删除注释和xx章
#         chapter="第.*章.*\n"
#         annote="\[\d*\] .*\n"
#         enter="(\n)+"
#         repl=''
#         for c in clist:
#             c=re.sub(enter, "\n", c)
#             c=re.sub(chapter, repl, c)
#             c=re.sub(annote,repl,c)
#             f2.write("\"{}\",".format(c))
#     print("ok")
# f2.write("\"\"]")
# f2.close()
############################################
#endregion
        


