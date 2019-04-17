def collatz1(number):
    if number%2==0:
        return number//2
    elif number%2==1:
        return 3*number+1

a = input('Please enter a integer:')
try:
    a= int(a)
except ValueError:
    print('Wrong Value\n')
else:
    number=collatz1(int(a))
    print(number)
    while number != 1:
        number = collatz1(number)
        print(number)





