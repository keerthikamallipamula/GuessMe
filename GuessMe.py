import random
guess_chances = 3
guess_count = 0
random_number = random.randint(1, 10)
while True:
    while guess_count < guess_chances:
        guess_number = int(input("Guess number from 1 to 10 : "))
        guess_count += 1
        if guess_number == random_number:
            print("You Win!!!!")
            break
    else:
        print(f'Sorry your guess is wrong, The number is {random_number}')
    try_again=input("Do you want to try again? (Y/N) : ")
    if try_again.upper() == "N":
        break
    else:
        guess_count = 0

