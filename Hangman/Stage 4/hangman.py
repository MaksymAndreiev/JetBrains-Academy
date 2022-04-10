# Write your code here
import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
wordh = word[:3] + "-" * len(word[3:])
guess = input("Guess the word {}: ".format(wordh))
if guess == word:
    print("You survived!")
else:
    print("You lost!")
