from user import User

user1 = User(
    first_name='Azim',
    last_name='Ochilov',
    email='azimochilov@gmail.com',
    password='Yaironman@.26',
    username='azimazim',
    balance=0
)
user2 = User(
    first_name='Ronaldo',
    last_name='Cristiano',
    email='criss@gmail.com',
    password='Yaironman@.26',
    username='criss',
    balance=1000
)


list_user = []

list_user.append(user1)
list_user.append(user2)

while 1:
    val = int(input("click!  "))
    if(type(val) == int):
        user2.balance += 1000
        print(user2.balance)
    if(type(val) == str):
        print(user2.balance)
        break







