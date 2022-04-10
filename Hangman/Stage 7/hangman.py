# Write your code here
import random

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
word_h = "-" * len(word)

moves = 8
guess_set = set()
while moves:
    print()
    print(word_h)
    guess = input("Input a letter: ")

    if len(guess) != 1:
        print("You should input a single letter")
        continue
    if not guess.islower():
        print("Please enter a lowercase English letter")
        continue

    if guess in word:
        temp = word_h
        word_h = "".join([guess if word[i] == guess else word_h[i] for i in range(len(word))])
        if temp == word_h:
            print("You've already guessed this letter")
            # moves -= 1
        if "-" not in word_h:
            # print()
            # print(word_h)
            print("You guessed the word {}!\nYou survived!".format(word_h))
            break
    else:
        if guess in guess_set:
            print("You've already guessed this letter")
            continue
        print("That letter doesn't appear in the word")
        moves -= 1
    guess_set.add(guess)
    # print()

if "-" in word_h:
    print("You lost!")
