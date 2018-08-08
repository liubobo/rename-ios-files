#encoding=utf-8
import os,sys
new_prefix = sys.argv[1]
path = sys.argv[2]

print sys.argv[1] 
print sys.argv[2] 


dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
   print file
   os.rename(path+'/'+file,path+'/'+new_prefix+'_'+file)

