import random
computer = random.randint(1, 100)
user = input("请输入您猜的数字")
user = eval(user)
if user == computer:
    print("Your right!")
elif user < computer:
    print("Make it bigger!")
elif user > computer:
    print("Make it smaller!")
while user != computer:
    user = input("请输入您猜的数字")
    user = eval(user)
    if user == computer:
        print("Your right!")
    elif user < computer:
        print("Make it bigger!")
    elif user > computer:
        print("Make it smaller!")

