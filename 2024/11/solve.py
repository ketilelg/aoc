import sys
import copy

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = list(f.read().strip().split(" "))

p1=p2=0

def blink(num,gen):
    global p1
    if(gen==25):
        p1+=1
    else:
#        print("bb",num,gen,len(num),gen)
        if num=="0":
            blink("1",gen+1)
        elif len(num)%2 == 0:
            blink(str(int(num[:int(len(num)/2)])),gen+1)
            blink(str(int(num[int(len(num)/2):])),gen+1)
        else:
            blink(str(2024*int(num)),gen+1)
            


for i in inp:
    print("i",i)
    blink(i,0)



print("1:",p1)
print("2:",p2)
