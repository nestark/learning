def bubblesort(a):
    lenth = len(a)-1

    for n in range(lenth):
        for i in range(lenth-n):
            if a[i] > a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    print(a)

mes = input('Please input a list of number, divided by commas:')
nums = list(int(x) for x in mes.split(sep=','))
print(nums)
bubblesort(nums)