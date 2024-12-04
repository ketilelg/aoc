import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    map = list(map(list,f.read().strip().split("\n")))

p1=0
p2=0

w=len(map)
h=len(map[0])

for y in range(w):
    for x in range(h):
        if(map[y][x]=="X"):
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    if ((0<= x+dx*3 < w)
                        and (0 <= y+dy*3 < h)
                        and (map[y+dy*1][x+dx*1]+
                             map[y+dy*2][x+dx*2]+
                             map[y+dy*3][x+dx*3] == "MAS")):
                        p1+=1

    
for x in range(1,w-1):
    for y in range(1,h-1):
        if(map[y][x]=="A"):
            if (map[y-1][x-1] + map[y+1][x+1] in ["MS","SM"] and
                map[y+1][x-1] + map[y-1][x+1] in ["MS","SM"]):
                p2+=1


print("1:",p1)
print("2:",p2)
