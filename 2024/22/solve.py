import sys
from functools import cache

with open(sys.argv[1] if (len(sys.argv) > 1) else 'input') as f:
    inp = list(map(int,f.read().strip().split("\n")))
            
def solve(num,gens):
    for i in range(gens):
        num= 16777215 & ((num<<6)^num)
        num= 16777215 & ((num>>5)^num)
        num= 16777215 & ((num<<11)^num)
    return num        

# def solve2(num,tc):
#     iters=0

#     changes=[]
#     while iters<4:
#         pnum=num
#         num= 16777215 & ((num<<6)^num)
#         num= 16777215 & ((num>>5)^num)
#         num= 16777215 & ((num<<11)^num)
#         ones=num%10
#         pones=pnum%10
#         changes.append(ones-pones)
#         iters+=1
# #        print("cc",changes)
#     while iters<2000 and tc!=changes:
#         pnum=num
#         num= 16777215 & ((num<<6)^num)
#         num= 16777215 & ((num>>5)^num)
#         num= 16777215 & ((num<<11)^num)
#         ones=num%10
#         pones=pnum%10
#         changes.pop(0)
#         changes.append(ones-pones)
# #        print(" s2l",ones,pones,changes,iters)
#         iters+=1
    
# #    print("s2r",iters,ones)
#     if tc==changes:
#         return(ones)
#     else:
#         return(0)

def gencstr(num):
    #returns changestr, and matching pricelist for a given num
    iters=0

    changes="" #-9=a, -8=b, etc
    prices=[num%10]

    while iters<2000:
        pnum=num
        num= 16777215 & ((num<<6)^num)
        num= 16777215 & ((num>>5)^num)
        num= 16777215 & ((num<<11)^num)
        ones=num%10
        pones=pnum%10
        changes = changes + chr(107+(ones-pones))
        prices.append(ones)
        iters+=1
    
    return changes,prices

p1=p2=0
p2r=[]
changes=[]
prices=[]
for n in inp:
    p1+=solve(n,2000)
#    print("ff",n,solve(n,2000))
#    print("s2",solve2(n,[-2,1,-1,3]))
    c,p=gencstr(n)
    changes.append(c)
    prices.append(p)

# print("sdfsdf",changes,prices)

for pp1 in range(-9,10):
    print("p1",pp1)
    for pp2 in range(-9,10):
#        print("p2",pp2)
        for pp3 in range(-9,10):
            for pp4 in range(-9,10):
                rrr=0
                cstr=chr(pp1+107)+chr(pp2+107)+chr(pp3+107)+chr(pp4+107)
                for i in range(len(changes)):
                    cp=changes[i].find(cstr)
                    if cp>0:
#                        print("  ffp",len(changes[i]),len(prices[i]),rrr,i,cp,cstr,pp1,pp2,pp3,pp4)
                        rrr+=prices[i][cp+4]
                if rrr>p2:
                    p2=rrr
                    p2r=[pp1,pp2,pp3,pp4]
        print("p2...",pp2,p2,p2r)


print("1:",p1)
print("2:",p2,p2r)
#1995 too low
#5000 (guess) too high