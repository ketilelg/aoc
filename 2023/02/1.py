import re
sum=0
sum2=0

with open('input') as f:
    for line in f:
        line=line.strip()
#       print("input",line)

        gid,games=line.split(":")
        game=int(gid.split()[1])
        ok=True
        minr=0
        ming=0
        minb=0
        
        for sg in games.split(";"):
            for sgc in sg.split(","):
                red=0
                green=0
                blue=0

                n,c=sgc.split()
                num=int(n)
#                print("num",num,"c",c)
                if "red" in c:
                    red+=num
                if "green" in c:
                    green+=num
                if "blue" in c:
                    blue+=num
                if(red>minr):
                    minr=red
                if(green>ming):
                    ming=green
                if(blue>minb):
                    minb=blue
                
#                print("r",red,"b",blue,"g",green)
                if not ((red <= 12) & (green <= 13) & (blue <=14)):
#                    print("yep, game",game)
#                else:
                    ok=False
        if(ok):
            sum+=game
        p=minr*ming*minb
#        print("power",p,minr,ming,minb)
        sum2+=p
                   
# 209 for lavt

print("1:", sum)
print("2:", sum2)
