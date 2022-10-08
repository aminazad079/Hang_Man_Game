import random
from hangman_art import stages,logo
from hangman_words import word_list
end_of_game=False
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
lives=6
print(logo)
print(chosen_word)

display=[]
for _ in range(word_length):
  display+='_'
print(display)

while not end_of_game:
  guess=input("Guess a letter: ").lower()

  if guess in display:
    print("you have already guesed this word, please chosse another: ")

  for postion in range(word_length):
    letter=chosen_word[postion]
    if letter==guess:
      display[postion]=letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, thats not in the word. youu lose a life.")
    lives-=1
    if lives==0:
      end_of_game=True
      print("Sorry, You lose")

  print(display)
  if "_" not in display:
    end_of_game=True
    print("Congratulations! you Win!")

  print(stages[lives])