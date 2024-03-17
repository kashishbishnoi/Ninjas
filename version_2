print("\nWELCOME TO THE GAME !!!")
print("THIS GAME GIVES THE USER 10 CHANCES TO GUESS A WORD.")
print("THE USER WILL GET 1 HINT CHANCE IF CHOSEN.") 

import random

words = {
    "Australia": "THE COUNTRY WHICH IS THIRD MOST POPULAR IN WORLD....",
    "Malawi": "The indigenous ethnic groups of it have a rich tradition of basketry",
    "Brazil": "Soccer is the most popular sport of this country",
    "Norway": "It is a Nordic country in Northern Europe, situated on the Scandinavian Peninsula.",
    "Canada": "CN TOWER is the most famous in this country",
    "Denmark": "It is almost entirely surrounded by water, which makes sense when you consider its Viking history.",
    "Serbia": "It is home to roughly 7 million inhabitants and it lies at the crossroads of Southeast and central Europe. Belgrade, the capital of Serbia is ranked among the largest and oldest cities in southeastern",
    "Monaco": "It is a small-city state on the French Riviera, known as a 'Billionaires' Playground. It is famous for its grand casinos, designer shopping centers, opulent bars and clubs, and a human-made beach",
    "Qatar": "It was described as a famous horse and camel breeding centre during the Umayyad period.",
    "India": "It is known for its diverse culture, history, natural landscapes, languages, classical dances, Bollywood, spirituality, natural beauty, and warm, welcoming citizens."
}

choice = "y"
c = 0
i = 0
figure = [
    '''
    
    +---+
       |
       |
       |
      ===''',
    '''
      
   +---+
   O   |
       |
       |
      ===''', 
    '''
   +---+
   O   |
   |   |
       |
      ===''',
    '''
   +---+
   O   |
  /|   |
       |
      ===''', 
    '''
   +---+
   O   |
  /|\  |
       |
      ===''',
    '''
   +---+
   O   |
  /|\  |
  /    |
     ===''',
    '''
   +---+
   O   |
  /|\  |
  / \  |
     ==='''
]

while choice == "y":
    guess = 0
    word = random.choice(list(words.keys()))
    word_hint = words[word]
    word_length = len(word)
    guesses = 0
    
    print("\n\nWELCOME TO THE GAME !!!")
    print("GUESS A WORD AND TRY TO FILL ")
    for k in range(word_length):
        print("_ ", end='')
    print("\n")
    
    for j in range(10):
        c += 1
        letter = input("Enter any letter: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue
        
        if letter in word.lower():
            print("You are one step closer!")
            print("KEEP IT UP!")
            print("Attempts left:", 10 - c)
            guesses += word.lower().count(letter)
            if guesses == word_length:
                print("\nWELL DONE")
                print("CONGRATULATIONS!")
                print("YOU SUCCEEDED!")
                break
        else:
            print("\nBetter luck next time")
            print("Attempts left:", 10 - c)
            print(figure[i])
            i += 1
            if i >= len(figure):
                print("\nOH! YOU LOST")
                print("****************Game Ended******************")
                break
            
            hint_choice = input("Want a hint? Enter 'y' for yes and 'n' for no: ")
            if hint_choice.lower() == "y":
                print(word_hint)
                
    choice = input("\nEnter 'y'  if you want to continue playing or 'n' for exit: ")
