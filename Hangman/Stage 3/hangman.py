# Write your code here
import random
print("H A N G M A N")
words = ['python', 'java', 'swift', 'javascript']
word = random.choice(words)
guess = input("Guess the word: ")
if guess == word:
    print("You survived!")
else:
    print("You lost!")
