import random
def random_number_by_comp():
    num = random.randint(1, 10)
    return num

def gues_the_number_by_comp(number):
    count = 0
    while 1:
        guess = random_number_by_comp()
        if guess == number:
            count += 1
            return count
        if guess > number:
            print("Too high!")
            count += 1
            continue
        if guess < number:
            print("Too low!")
            count += 1
            continue

def game():
    print("you have 2 options ")
    print("1. Guess the number by yourself")
    print("2. Guess the number by computer")
    count1 = 0
    count2 = 0
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        number = random_number_by_comp()
        while 1:
            your_number = int(input("Enter your guess: "))
            if your_number == number:
                count1 += 1
                break
            if your_number > number:
                print("Too high!")
                count1 += 1
            if your_number < number:
                print("Too low!")
                count1 += 1

    elif(choice == 2):
        number = int(input("Enter number: "))
        count2 = gues_the_number_by_comp(number)


    if(count1 == count2):
        print("DRAW!")
    elif(count1 < count2):
        print(f"YOU WON {count1} ")
        print(f"COMPUTER'S SCORE {count2}")
    elif(count1 > count2):
        print(f"COMPUTER WON {count2} ")
        print(f"YOUR SCORE {count1}")

game()