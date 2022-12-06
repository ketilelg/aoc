#!/usr/bin/python3
with open('input') as f:
    for line in f:
        s=line.strip()
        i=0
        while i<(len(s)-14):
            ss=set(s[i:i+14])
            print("t:",ss)
            if len(ss)==14:
                print("hoi",ss,i+14)
                break
            i+=1


