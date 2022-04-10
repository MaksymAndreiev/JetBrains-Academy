# Write your code here
import random

print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
wordh = "-" * len(word)

moves = 8
while moves:
    print(wordh)
    guess = input("Input a letter: ")
    if guess in word:
        wordh = "".join([guess if word[i] == guess else wordh[i] for i in range(len(word))])
    else:
        print("That letter doesn't appear in the word")
    moves -= 1
    print()

print("Thanks for playing!\nWe'll see how well you did in the next stage")
