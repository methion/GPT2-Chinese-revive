from watermarker.marker import add_mark
import os

indir=r"C:\Users\dell\Downloads\\ai"

file_n=os.listdir(indir)
print(file_n)
outdir=r"C:\Users\dell\Downloads\\aiout"

files = os.listdir(indir)
print(files)
for file in files:
    add_mark(file=indir+"\\"+file, out=outdir,mark='ai is sb',
    color="#DCDCDC",opacity=0.2,angle=30,space=75)