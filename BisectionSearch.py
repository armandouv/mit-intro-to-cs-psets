print("Please think of a number between 0 and 100!")
low = 0
high = 100
comp = True

while (comp):
    guess = (high + low)//2
    print("Is your secret number", str(guess), "?", end = ' ')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    check = input()
    if check == 'c':
        break
    elif check == 'h':
        high = guess
    elif check == 'l':
        low = guess
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was:", guess)