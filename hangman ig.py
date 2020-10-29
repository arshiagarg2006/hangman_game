import time
name = input("what is your name?")
print(f"welcome {name}, you are playing hangman")
time.sleep(1)
print ("start the guess")
time.sleep(0.5)
word = "compass"
guesses = ''
turns = 10

while (turns > 0):
    failed = 0
    for char in word:
        if char in guesses:
            print (char)
        else:
            print ("_")
            failed += 1
    if failed == 0:
        print ("winnings")
        break
    guess = input("guess character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print ("wrong")
        print (f"you have {turns} more guesses left")
    if turns == 0:
        print ("you lose")
