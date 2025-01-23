import sys

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

p1=0
p2=0

# inp=inp+" "

# def cstr(istr):
#     n=1
#     c=istr[:1]
#     istr=istr[1:]
#     nc=istr[:1]
#     istr=istr[1:]
#     rstr=""
#     while True:
# #        print("w",c,n)
#         if c==nc:
#             n+=1
#         else:
#             rstr+=str(n)+c
#             n=1
#         c=nc
#         if not istr:
#             return rstr
#         nc=istr[:1]
#         istr=istr[1:]

def cstr(istr):
    nc=istr[:1]
    istr=istr[1:]
    n=1
    rstr=""
    for c in istr:
        if c==nc:
            n+=1
        else:
            rstr+=str(n)+nc
            n=1
        nc=c
    return rstr+str(n)+nc

s=inp
for i in range(40):
    s=cstr(s)
#    print("sdf",i,len(s))

print("1:",len(s)) 

for i in range(10):
    s=cstr(s)
#    print("sdf",i,len(s))

print("2:",len(s))
