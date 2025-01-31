maxrow=row=col=1
num=20151125
done=False
while not done:
    num=(num*252533)%33554393
    col+=1
    row-=1
    if row==0:
        row=maxrow+1
        maxrow=row
        col=1
        print(" ---",num,col,row)
    if row==2978 and col==3083:
        done=True
        
print("1:",num)
