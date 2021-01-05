passward = 1234
money = 50000
myinput = 0
try:
    a = int(input("Enter a ATM Password:"))
except Exception as e:
    print(e)

if a == passward:
    if myinput <= money:

        myinput = int(input("Enter a Amount:"))

        mybalance = money - myinput
    print("Your Balance is:", mybalance)


