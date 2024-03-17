# HANGMAN GAME
print("\nWELCOME TO THE GAME !!!")
print("THIS GAME GIVES THE USER 10 CHANCES TO GUESS A WORD.")
print("THE USER WILL GET 1 HINT CHANCE IF CHOSEN.") 

import random

words = {
    "Chile": " Chilean cuisine is known for its delicious dishes including seafood specialties ",
    "Brazil": "Soccer is the most popular sport of this country.",
    "Norway": "It is a Nordic country in Northern Europe.",
    "Denmark": "It is known for its cycling-friendly infrastructure and culture",
    "Serbia": "It is predominantly Orthodox Christian.",

    "Mexico": "It has produced influential cultural figures such as artists Frida Kahlo",
    
}



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

choice = "y"
while (choice == "y"):
    listt=[]
    guess = 1
    word = random.choice(list(words.keys()))
    a=word.split()
    print(word)
    word_hint = words[word]
    word_length = len(word)
    guesses = 0
    li=['','','','','','','','','','']
    
    print("\n\nWELCOME TO THE GAME !!!!")
    print("GUESS A WORD AND TRY TO FILL ")
    for k in range(word_length):
        print("_ ", end='')
        li[k]='_'
    print("\n")
    list1=['_','_','_','_','_','_','_','_','_','_']
    for j in range(10):
        
        letter = input("Enter any letter: ").lower()
        c += 1
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue
        cy=0
        
        if letter in word.lower():
            cy=cy+1
            index=word.lower().index(letter)
            if cy<=1:
                index=word.lower().index(letter)
                list1[index]=letter
                listt.append(letter)
            else:
                
                t=word.lower().find(letter)
                if t!=index:
                    list1[t]=letter
                    listt.append(letter)
            
            for q in range(len(word)):
                print(list1[q],end=' ')
            if '_ ' not in li:
                print("\n\nYou are one step closer!")
                print("KEEP IT UP!")
            if 10-c==1:
                o1='①'
            elif 10-c==2:
                o1='②'          
            elif 10-c==3:
                o1='③'
            elif 10-c==4:
                o1='④' 
            elif 10-c==5:
                o1='⑤'
            elif 10-c==6:
                o1='⑥'
            elif 10-c==7:
                o1='⑦'
            elif 10-c==8:
                o1='⑧'
            elif 10-c==9:
                o1='⑨'
            print("                                             Attempts left:", o1)
            if letter in listt:
                listt.remove(letter)
                guesses += word.lower().count(letter)
                if listt==[]:
                    if guesses == word_length:
                    
                        print("\n!!!!!!!WELL DONE!!!!!!!")
                        print("🏆CONGRATULATIONS!🏆")
                        print("YOU SUCCEEDED!")
                        print("******GAME ENDED******")
                        break
                
                    
        else:
            oa=0
            print("Incorrect!!!!!!!")
            print("TRY AGAIN\n\n")
            if 10-c==1:
                oa='①'
            elif 10-c==2:
                oa='②'          
            elif 10-c==3:
                oa='③'
            elif 10-c==4:
                oa='④' 
            elif 10-c==5:
                oa='⑤'
            elif 10-c==6:
                oa='⑥'
            elif 10-c==7:
                oa='⑦'
            elif 10-c==8:
                oa='⑧'
            elif 10-c==9:
                oa='⑨'
            
            print("                                             Attempts left:", oa)
            print(figure[i])
            i += 1
            if i >= len(figure):
                print("\nOH! YOU LOST")
                print("****************Game Ended******************")
                break
            
            hint_choice = input("Want a hint?\nEnter 'y' for yes and 'n' for no: ")
            if hint_choice.lower() == "y":
                print(word_hint)
    c=0           
    choice = input("\nEnter 'y'  if you want to continue playing or 'n' for exit: ")
    if choice.lower() != "y":
        break

