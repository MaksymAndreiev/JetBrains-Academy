import random

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
wordh = "-" * len(word)

moves = 8
while moves:
    print()
    print(wordh)
    guess = input("Input a letter: ")
    if guess in word:
        temp = wordh
        wordh = "".join([guess if word[i] == guess else wordh[i] for i in range(len(word))])
        if temp == wordh:
            print("No improvements")
            moves -= 1
        if "-" not in wordh:
            print()
            print(wordh)
            print("You guessed the word!\nYou survived!")
            break
    else:
        print("That letter doesn't appear in the word")
        moves -= 1
    #print()

if "-" in wordh:
    print("You lost!")
