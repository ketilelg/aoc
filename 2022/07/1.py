#!/usr/bin/python3

sumlt=0
free=70000000
needed=30000000
sml=1000000000

def rec(f,d):
   global sumlt
   global free
   global needed
   global sml
   size=0

   for line in f:
      if line.find("$ cd /")>=0:
         dir=line.split()[2]
      elif line.find("$ cd ..")>=0:
         dir=line.split()[2]
         return(size)
      elif line.find("$ cd")>=0:
         dir=line.split()[2]
         ss=rec(f,d+"/"+dir)
         size+=ss
         if(ss<=100000):
            sumlt+=ss
         if (ss<sml) and (ss+free>=needed):
            sml=ss
      elif line.find("$ ls")>=0:
         pass
      elif line.find("dir ")>=0:
         pass
      else:
         sz,nm=line.split()
         size+=int(sz)
   return(size)


with open('input') as f:
   totsize=rec(f,"")
f.close()
print("p1",sumlt)   
free-=totsize
sml=1000000000
with open('input') as f:
   totsize=rec(f,"")
print("p2",sml)



 
