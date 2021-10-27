# -*- coding: utf-8 -*-
import PyPDF2
import re
import glob, os
import sys
import time
import shutil
from os import path
import os

directory = "Client1"
directory1 = "Client2"
directory2 = "Client3"
directory3 = "Client4"
directory4 = "Client5"
directory5 = "Client6"
directory6 = "Client7"

parent_dir = "C:/Users/VitorAssuncaoCrosera/Desktop/SORT/"

list=[directory,directory1,directory2,directory3,directory4,directory5,directory6]
for item in list:
    path=os.path.join(parent_dir, item)
    os.mkdir(path)


print("Folders Created")
time.sleep(2)


lst = list()
i=0


time.sleep(2)
print("Waiting...")
print("Waiting...")
mypath = r"C:\Users\VitorAssuncaoCrosera\Desktop\SORT"

for file in glob.glob(mypath + "/*.pdf"):

    pdfReader = PyPDF2.PdfFileReader(file)

    #print(pdfReader.numPages)

    pageObj = pdfReader.getPage(0)

    lines = pageObj.extractText()
    #print(lines)

    lst.append(lines[231:260])

new_lst = list()

for string in lst:
    new_lsts = string.replace("/","-")
    new_lst.append(new_lsts)
    #print(new_lst)

new_lsts = list()
for trings in new_lst:
    new_lstss = trings.replace("\n"," ")
    new_lsts.append(new_lstss)
    #print(new_lsts)

path = r'C:\Users\VitorAssuncaoCrosera\Desktop\SORT'
while i<len(new_lsts):
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            my_source = path + "\\"+ filename
            #print(my_source)
            my_dest = path + "\\" + str(new_lsts[i]) + " " + filename
            #print(my_dest)
            os.rename(my_source,my_dest)
            i+=1


time.sleep(2)
print("Be Patient")


for filename in os.listdir(path):
    try:
        if filename.startswith("Clint1"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client1" + "\\" + filename
            shutil.move(source,destination)
        elif filename.startswith("Client2"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client2" + "\\" + filename
            shutil.move(source,destination)
        elif filename.startswith("Client3"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client3" + "\\" + filename
            shutil.move(source,destination)
        elif filename.startswith("Client4"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client4" + "\\" + filename
            shutil.move(source,destination)
        elif filename.startswith("Client5"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client5" + "\\" + filename
            shutil.move(source,destination)
        elif filename.startswith("Client6"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client6" + "\\" + filename
            shutil.move(source,destination)
        elif filename.startswith("Client7"):
            source = path + "\\" + filename
            destination = path + "\\" + "Client7" + "\\" + filename
            shutil.move(source,destination)

        else:
            pass
    except:
        pass

print("Well Done")
