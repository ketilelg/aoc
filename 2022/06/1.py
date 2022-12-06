#!/usr/bin/python3
with open('input') as f:
    for line in f:
        s=line.strip()
        i=0
        while i<(len(s)-4):
            ss=set(s[i:i+4])
            print("t:",ss)
            if len(ss)==4:
                print("hoi",ss,i+4)
                break
            i+=1


