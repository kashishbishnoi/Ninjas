PROJECT TITLE - Hangman Project Game
Description : This project is a Hangman Project Game.It is a guessing game for two or more players.Here, we have designed it for single user. The player thinks of a word and tries to guess it by suggesting letters. If the user is able to guess the word correctly , the user wins. The objective of the game is to expand vocabulary through playing with words, making it a fun way of learning.
TEAM MEMBERS : 
Leader : Muskan Punia (2310990743)
Developer : Harshita Lamba (2310990687)
Tester: Kashish (2310990710)

Instructions for running the game:
Our code generates a random word based on a theme, which has to be guessed by the player. The screen will display blanks (short lines) for each letter of the word. Then the player is asked to guess a letter, if the letter appears in the word, the blanks get replaced by the letter at everyplace it appears in the word. If the guessed letter does'nt exist in the word,we cross out the lifelines, which are basically the number of chances.The player will continue guessing the letters until he/she guesses the whole word or loses the game.To make it interesting, we have added a hangman figure. As the player guesses a wrong letter, one element gets added to the hangman. If the user loses, the screen displays the whole diagram of a hangman.

VERSION-1:
The approach is good, but there are few errors I'd like to highlight:
1. The number of attempts should'nt be decremented, if the guessed letter is correct.Attempts should only be reduced by one, if the user makes a wrong guess.
2. Once the player guesses the whole word correctly, the program is supposed to declare the user as winner. However, the code is still running until the number of chances reduces to zero. Then, it asks the user if they want to play again without telling them if they won or lose.
3. The figures of hangman are there in the code, but they are not being displayed on the screen as and when required, which needs to be done in the right way. As the name suggests, the game revolves around hangman, so the errors must be rectified to make the figures visible.


