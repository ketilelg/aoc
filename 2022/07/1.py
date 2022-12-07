#!/usr/bin/python3

sumlt=0
#the uglyness: hardcode data..
free=70000000-42558312
needed=30000000
sml=1000000000

def rec(f,d):
   global sumlt
   global free
   global needed
   global sml
   print("rec",d)
   size=0
   for line in f:
      print("line:", line)
      if line.find("$ cd /")>=0:
         dir=line.split()[2]
         print("cd/",dir)
      elif line.find("$ cd ..")>=0:
         dir=line.split()[2]
         print("cd-",dir)
         print("end",d,size)
         return(size)
         return size
      elif line.find("$ cd")>=0:
         dir=line.split()[2]
         print("cd",dir)
         ss=rec(f,d+"/"+dir)
         size+=ss
         if(ss<=100000):
            print("less than",ss)
            sumlt+=ss
         if (ss<sml) and (ss+free>=needed):
            print("smaller:",sml)
            sml=ss
      elif line.find("$ ls")>=0:
         print("ls")
      elif line.find("dir ")>=0:
         print("dir..")
      else:
         sz,nm=line.split()
         size+=int(sz)
         print("file:",nm,sz,size)
   print("end",d,size)
   return(size)


with open('input') as f:
   totsize=rec(f,"")
print("totalsize:",totsize)
print("p1",sumlt)   
print("p2",sml)



 
