# This is a game that allows you to guess a number three times before rewarding you 
secret_number = 9
guess_count = 0
Guess_limit = 3
while guess_count < Guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print('Sorry, you failed!')
