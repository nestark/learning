a=[12,2,3,5,4,8,23,14,7,21]
for n in range(9):
    while n<9:
        if a[n]>a[n+1]:
            b=a[n+1]
            a[n+1]=a[n]
            a[n]=b
            n+=1
        else:
            n+=1
print(a)
