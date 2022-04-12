# Write your code here
import random

win_count = 0
loss_count = 0


def gameplay():
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    word_h = "-" * len(word)

    moves = 8
    guess_set = set()
    while moves:
        print()
        print(word_h)
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if not guess.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if guess in word:
            temp = word_h
            word_h = "".join([guess if word[i] == guess else word_h[i] for i in range(len(word))])
            if temp == word_h:
                print("You've already guessed this letter.")
            if "-" not in word_h:
                print("You guessed the word {}!\nYou survived!".format(word_h))
                global win_count
                win_count += 1
                break
        else:
            if guess in guess_set:
                print("You've already guessed this letter")
                continue
            print("That letter doesn't appear in the word")
            moves -= 1
        guess_set.add(guess)

    if "-" in word_h:
        global loss_count
        loss_count += 1
        print("You lost!")


print("H A N G M A N")
while 1:
    opt = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
    if opt == "play":
        gameplay()
        print()
    elif opt == "results":
        print(f"You won: {win_count} times.\nYou lost: {loss_count} times.")
    elif opt == "exit":
        break
