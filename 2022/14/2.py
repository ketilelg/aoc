#!/usr/bin/python3

import numpy as np


miny = maxy=0
minx = maxx = 500
with open('input') as f:
    for line in f:
       for c in line.strip().split(" -> "):
          x,y=c.split(",")
          x=int(x)
          y=int(y)
          if x > maxx:
             maxx = x
          if x < minx:
             minx = x
          if y > maxy:
             maxy = y
          if y < miny:
             miny = y


h=maxy+3
w=(h*2+2)+(maxx-minx)
offs=h+1
map=np.chararray((w,h))

map[:]="."
for x in range(w):
   map[x][h-1]="#"

def printmap():
   for y in range(h):
      for x in range(w):
         print(map[x][y].decode(),end="")
      print("")
   print("")

with open('input') as f:
    for line in f:
       sx,sy=line.strip().split(" -> ")[0].split(",")
       sx=int(sx)-minx+offs
       sy=int(sy)-miny
       for c in line.strip().split(" -> "):
          x,y=c.split(",")
          x=int(x)-minx+offs
          y=int(y)-miny
          for xx in range(min(sx,x),max(sx,x)+1):
             for yy in range(min(sy,y),max(sy,y)+1):
                map[xx][yy]="#"

          sx=x
          sy=y

done=False
nus=0
while not done:
   sx=500-minx+offs
   sy=0
   done = map[sx][sy].decode() == "o"
   atrest=False
   while not atrest and not done:
      if map[sx][sy+1].decode() == '.':
         sy+=1
      else:
         if sx==0:
            done=True
         elif map[sx-1][sy+1].decode() == ".":
            sx-=1
            sy+=1
         elif sx == w-1:
            done=True
         elif map[sx+1][sy+1].decode() == ".":
            sx+=1
            sy+=1
         else:
            map[sx][sy]="o"
            atrest=True
            nus+=1

print("p2",nus)
