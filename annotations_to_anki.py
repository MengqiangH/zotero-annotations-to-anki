import os #用于改变系统工作路径
import re #正则表达式 

os.chdir("C:/Users/hu/Desktop") #改变工作路径到桌面
with open("2.txt","r",encoding='utf-8') as f:
    data = f.read() #读取.txt文件内容
    #print(data)
a1=r'#.*\n.*\n.*\n“'
data0 = re.sub(a1,'~“',data)
#print(data0)
a='\n'
data1 = re.sub(a,'',data0)
#print(data1)
b='~“'
data2 = re.sub(b,'\n|',data1)
#print(data2)
c='~'
data3 = re.sub(c,'|',data2)
#print(data3)
d='” \('
data4 = re.sub(d,'|',data3)
#print(data4)
e='\)\) \(\[pdf\]\('
data5 = re.sub(e,'|<a href="',data4)
#print(data5)
f='\|<'
data6 = re.sub(f,'">PAPER_LINK</a>|</div><',data5)
#print(data6)
g='\)\) '
data7 = re.sub(g,'">PAGE_LINK</a>',data6)
#print(data7)
h='\]\('
data8 = re.sub(h,']|<div><a href="',data7)
#print(data8)
i= '\n\|'
data9 = re.sub(i,'\n',data8)
#print(data9)
j='  '# 注释 
data10 = re.sub(j,'<br>',data9)
#print(data10)
k=' '
data11 = re.sub(k,'<br>',data10)
#print(data11)
f2 = open('anki.txt','w+',encoding='utf-8')
f2.write(data11)
f2.close()
