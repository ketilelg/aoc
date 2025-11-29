import sys
import hashlib

#with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
#    inp = f.read().strip().split("\n")

p1=""
p2="        "
#input="abc"
input="reyedfim"

idx=0

# for p in range(8):
#     found=False
# #    print("p",p,hashlib.md5(b"0").hexdigest())
#     while not found:
#         pw=input+str(idx)
#         hash=hashlib.md5(pw.encode()).hexdigest()
#         if hash[:5]=="00000":
#             found=True
#         idx+=1
#     print("hohoi",pw,hash)
#     p1+=hash[5]

while p2.find(" ")>=0:
    found=False
    while not found:
        pw=input+str(idx)
        hash=hashlib.md5(pw.encode()).hexdigest()
        p5=ord(hash[5])-ord("0")
        if hash[:5]=="00000":
#            print("hoi",hash,pw)
            if p5 in range(8):
                found=True
        idx+=1
    if p2[p5]==" ":
        np2=p2[:p5]+hash[6]+p2[p5+1:]
        p2=np2
        print("hohoi",p5,p2,pw,hash)

print("1:",p1)
print("2:",p2)
