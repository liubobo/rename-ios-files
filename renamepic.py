#encoding=utf-8
import os
path = "./"
new_prefix = 'mine'
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
   print file
   os.rename('./'+file,'./'+new_prefix+'_'+file)

