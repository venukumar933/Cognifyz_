import random
target= random.randint(1,100)
guess=0
while True:
    user_guess=int(input("enter a your guess:"))
    guess+=1
    if user_guess<target:
        print("Too low Try agaian")
    elif user_guess>target:
        print("Too high")
    else:
        print(f"Congratulations your guess is correct{target}in {guess} tries")
        break