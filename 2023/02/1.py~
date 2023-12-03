import re
sum=0
sum2=0
with open('input') as f:
    for line in f:
        line=line.strip()
        print("input",line)

#        digits = re.findall("\d",line)

        #        sum += int(re.search("^\D*(\d)\w+(\d)\D*$",line).group())
#        lv=int(digits[0])*10 + int(digits[-1])
#        sum=sum+lv

        
        fpos=len(line)
        d=0
        fd=0
        for sd in ["one","two","three","four","five","six","seven","eight","nine"]:
            d+=1
            fp=line.find(sd)
#            print("sd",sd,"d",d,"fp",fp,"fpos",fpos)
            if ((fp >= 0) & (fp < fpos)):
#                print("-match",fp,d)
                fpos=fp
                fd=d
                fs=sd
        ddd=re.search("\d",line)
        if (ddd):
            dst=ddd.start()
#            print("xxxx digit first")
        else:
#            print("xxxx word first")
            dst=len(line)
#        print("fpos",fpos,"fd",fd,"fs",fs,"dst",dst)
        if((fpos<len(line)) & (fpos < dst)) :
            line=line.replace(fs,str(fd),1)
#        print("after replace",line)



        fpos=-1 #position of best digit
        d=0 #digit, as int
        fd=0 #current best
        for sd in ["one","two","three","four","five","six","seven","eight","nine"]:
            d+=1
            fp=line.rfind(sd)
#            print("sd",sd,"d",d,"fp",fp,"fpos",fpos)
            if ((fp >= 0) & ((fp) > fpos)):
#                print("--match",fp,d)
                fpos=fp
                fd=d
                fs=sd
#        print("fpos",fpos,"fd",fd,"fs",fs)
        dst=re.search("\d\D*$",line).start()
#        print("dd",dst,"fpos",fpos)

        if((fpos>0) & (dst < fpos)):
            line=line.replace(fs,str(fd))
#        print("after replace2",line)

                
        
        digits = re.findall("\d",line)

        #        sum += int(re.search("^\D*(\d)\w+(\d)\D*$",line).group())
        lv=int(digits[0])*10 + int(digits[-1])
        sum2=sum2+lv
        print("line",line,"lv",lv)

#        sum=sum+int("".join(filter(str.isdigit, line)))

# 54307 er for høyt
# 54272 er feil
# 54266 er feil
# 54285 er feil

print("1:", sum)
print("2:", sum2)
