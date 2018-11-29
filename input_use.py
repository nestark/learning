mes= input("Hello,what's your name?\n")
print('Nice to meet you, '+mes)
flag=True
while flag:
    height = input("How tall are you, in inches? ")
    try:
        height = int(height)
    except ValueError:
        print('\nWrong input\n')
    else:
        if height >= 36:
            print("\nYou're tall enough to ride!")
        else:
            print("\nYou'll be able to ride when you're a little older.")
        flag=False
