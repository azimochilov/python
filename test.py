from decimal import Decimal, getcontext


users = []
users_cashes = []

n = int(input("Enter number of users: "))

for i in range(n):
    users.append(input("Enter username: "))

print("enter the money to their bank account\n")

for i in range(n):
    users_cashes.append(Decimal(input(f"enter {users[i]}'s money:  ")))


for i in range(n):
    print(f"{users[i]}'s bank account got this amount of money: {users_cashes[i]}")

print("do you wanna transfer your money to your frinend's account?"
      "if yes just type yes"
      "if not just type no")

value = input("your answer:  ")
amount = 0
if(value == "yes"):
    name1 = input("enter your name: ")
    name2 = input("enter name of your friend: ")
    for  i in range(n):
        if(users[i] == name1):
            print("how much u wanna give from your money?:  ")
            amount = Decimal(input(f"enter amount: "))
            users_cashes[i] -= amount

    for i in range(n):
        if(users[i] == name2):
            users_cashes[i] += amount


    print(f"{name1} gave to {name2} this amount of money: {amount}")

    for i in range(n):
        print(users[i])
        print(users_cashes[i])

else:
    print("have a good day!")
