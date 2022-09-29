# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:24:10 2022

@author: VGS2COB
"""

import os
import shutil

#print(os.environ.get('path'))
#print(os.environ["TMP"])
#path = os.chdir(r"C:\Users\VGS2COB\Practice\Project")
path = os.getcwd()
source = r"C:\Users\VGS2COB\Practice\projects"
destination = r"C:\Users\VGS2COB\Practice\vignesh"
#print(os.getlogin())
#print(os.getppid())
#print(os.listdir(path))

lst1 = []

with open('Trial111.txt') as f:
    line = f.readlines()
    print(line)
    print("Splited lines are",line[0].splitlines())
    
    
    if (line[0].splitlines() == ['pass']):
        print("Passed")
    else:
        print("Did not execute")
    

for roots,dirs,files in os.walk(source):
    for file in files:
        print(file.endswith('html'))
        if file.endswith('.html'):
            x ='1851'
            res = [i for i in files if x in i]
            if res:                
              print("The value of res is ",str(res[0]))
              print("The value of file is : ",file)
              source_file = source + '\\' + str(res[0])
              destination_file = destination + '\\' + str(res[0])
              print("The source file is :",source_file)
              print("The destination file is :",destination_file)
              #a = os.path.isfile(str(res))
              #print("THe value of a is ", a)
              if str(res[0]) not in lst1:
                  if os.path.isfile(source_file):
                      shutil.copyfile(source_file,destination_file)
                      print('Copied :',file)
                      os.rename(destination_file,r"C:\Users\VGS2COB\Practice\vignesh\LCMT_Absolute_Values.html")
                      lst1.append(str(res[0]))
                      print("The lst1 container : ",str(res[0]))
                        
        if file.endswith('.html'):
            x ='0908'
            print('The value of res after 1st test case is :', res)
            res = [i for i in files if x in i]
            if res:                
              print("The value of res is ",str(res[0]))
              print("The value of file is : ",file)
              source_file = source + '\\' + str(res[0])
              destination_file = destination + '\\' + str(res[0])
              print("The source file is :",source_file)
              print("The destination file is :",destination_file)
              #a = os.path.isfile(str(res))
              #print("THe value of a is ", a)
              if str(res[0]) not in lst1:
                  if os.path.isfile(source_file):
                      shutil.copyfile(source_file,destination_file)
                      print('Copied :',file)
                      os.rename(destination_file,r"C:\Users\VGS2COB\Practice\vignesh\LCMT_Ays.html")
                      lst1.append(str(res[0]))
                      print("The lst1 container : ",str(res[0]))
              
        if file.endswith('.html'):
            print("Code yet to be written")
                         
                         
                        
        else:
            print("There is no HTMl file available in the folder")
            break
    break

print("Came out of the loop")
                    
        
                
##to check in file.

           

                
       

    