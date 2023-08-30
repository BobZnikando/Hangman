import random

random_words = 'apple banana strawberry music piano guitar elephant lizard'

random_words = random_words.split(' ')
word = random.choice(random_words)

x = 0
tries = 0
unique_characters = set(word)
y = len(unique_characters)

already_guessed = ''

print('WELCOME!\nType the letters and guess the word :)\n')

for i in word:
    print('_', end=' ')
#print('\n')
while x != y:
    guess = input('\nGuess the letter: ')

    tries += 1
    if guess in word:
        already_guessed += guess
        x += 1
    for i in word:
        if i in already_guessed:
            print(i, end=' ')
        else:
            print('_', end=' ')


print('\n\nYOU WON in:', tries, 'tries')
