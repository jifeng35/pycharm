products = [['iphone', 6888], ['mac', 10000], ["小米11", 4899], ["coffee", 11], ["death", 198]]
print("-"*20)
print("\t\t商品如下:")
for i in products:
    print("商品名为:", i[0], end="")
    print("\t价格为:", i[1])
print('-'*20)
i = 1
buy_car = []
while i:
    wanna_buy = input()
    if wanna_buy == 'q':
        i = 0
    elif(not(wanna_buy.isdigit())) or eval(wanna_buy) > len(products):
        print("Fail to add in your wanna_buy!")
    else:
        buy_car.append(products[eval(wanna_buy)-1])
        print(f"you have just buy a {products[eval(wanna_buy)-1][0]}")
sum1 = 0
if len(buy_car):
    for i in buy_car:
        sum1 += i[1]
        print("商品名为:", i[0], end="")
        print("\t价格为:", i[1])
    print("总价为:", sum1, "rmb")
else:
    print("You do not buy anything!")
