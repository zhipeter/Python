import os
import shutil

string=input("输入日期：")
path='E:\\Camera360\\2017\\'+str(string)
0
int=[0,0,0,0,0,0,0]
for root,dirs,files in os.walk(path):
      for name in files:
            fname,fext=os.path.splitext(name)
            file=os.path.join(root,name)
            dir=os.path.dirname(file)
            dirname=dir[-2:]
            if dirname=="动漫":
                  int[0]+=1
                  os.rename(os.path.join(root,name),os.path.join(root, "Anime"+str(int[0])+fext))
            elif dirname=="风景":
                  int[1]+=1
                  os.rename(os.path.join(root,name),os.path.join(root, "Screen"+str(int[1])+fext))
            elif dirname=="宽屏":
                  int[2]+=1
                  os.rename(os.path.join(root,name),os.path.join(root, "WidthScreen"+str(int[2])+fext))
            elif dirname=="美女":
                  int[3]+=1
                  os.rename(os.path.join(root,name),os.path.join(root, "Beauty"+str(int[3])+fext))
            elif dirname=="游戏":
                  int[4]+=1
                  os.rename(os.path.join(root,name),os.path.join(root, "Game"+str(int[4])+fext))
            elif dirname=="杂物" or dirname=="其他":
                  int[5]+=1
                  os.rename(os.path.join(root,name),os.path.join(root, "Other"+str(int[5])+fext))
            else:
                  int[6] += 1
                  os.rename(os.path.join(root, name), os.path.join(root, "Nothing"+str(int[6])+fext))

for root,dirs,files in os.walk(path):
      for name in files:
            shutil.move(os.path.join(root,name),path)