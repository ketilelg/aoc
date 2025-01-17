import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip().split("\n")

p1=p2=0

keyb=[[1,2,3],
      [4,5,6],
      [7,8,9]]

k2=[["*","*","1","*","*"],
    ["*","2","3","4","*"],
    ["5","6","7","8","9"],
    ["*","A","B","C","*"],
    ["*","*","D","*","*"]]

def limit(v,vmin,vmax):
    return max(vmin,min(vmax,v))

x=y=1
x2=0
y2=2
p2=p1=""
for k in inp:
    for c in k:
        match c:
            case "U":
                y-=1
                if y2>0 and k2[y2-1][x2]!="*":
                    y2-=1
            case "D":
                y+=1
                if y2<4 and k2[y2+1][x2]!="*":
                    y2+=1
            case "L":
                x-=1
                if x2>0 and k2[y2][x2-1]!="*":
                    x2-=1
            case "R":
                x+=1
                if x2<4 and k2[y2][x2+1]!="*":
                    x2+=1
        x=limit(x,0,2)
        y=limit(y,0,2)
    print("sdfsdf",x,y)
    p1+=str(keyb[y][x])
    p2+=k2[y2][x2]

print("1:",p1)
print("2:",p2)
