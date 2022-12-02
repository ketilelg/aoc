#!/usr/bin/python3

sum=0
max=0
with open('input') as f:
    for line in f:


        if (len(line)>1):
            v=int(line.strip())
            sum += v
        else:
            print(sum)
            if(sum > max):
                max=sum
            sum=0
print('max', max)            
