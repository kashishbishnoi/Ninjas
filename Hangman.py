# HANGMAN GAME
import random
words=["cat","bat","dad","net","maid","kit","dog","sim"]
choice="y"
c=0
i=0
figure=['''
    
    +---+
       |
       |
       |
      ===''','''
      
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''','''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''','''
   +---+
   O   |
  /|\  |
 /     |
     ===''','''
   +---+
   O   |
  /|\  |
  / \  |
       ==='''
]
w=random.choice(words) 
while(choice=="y"):
    for j in range(10):
        c=c+1

        
        letter=input("enter any letter").lower()
        if letter in w:
            print("Congratulations!")
            print("you are close")
            print("Attempts left:",10-c)
        else :
            print("Better luck next time")
            print("Attempts left:",10-c)
            
            
    choice=input("enter y if want to continue in game")
