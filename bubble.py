def bubblesort(a):
    lenth = len(a)-1
    for n in range(lenth):
        while n<lenth:
            if a[n] > a[n+1]:
                b = a[n+1]
                a[n+1] = a[n]
                a[n] = b
                n += 1
            else:
                n += 1
    print(a)


mes = input('Please input a list of number, divided by space:')
nums = list(int(x) for x in mes.split())
print(nums)
bubblesort(nums)