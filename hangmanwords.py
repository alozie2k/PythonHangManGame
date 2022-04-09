import hangmanparts
# imports the file that stores the functions that print out parts of the hangman
from textblob import Word
#allows the program to use textblob an api that can be use to spell check the words and make sure they are real
#Word being an in built project from textblob used to complete this process
import random
#allows the python program use the random function
f =open("words.txt")
#2. Read the words.txt file (which has words that the program can choose from) and store the lines into a string
textStr = f.read()
#3. Split the string into a list of words
words=textStr.split()

menu=input("One Player or Two Players(Enter One if one player Two if two players):  ")
while menu !="One" or "Two":
 if menu=="Two":
  player1 = input("player 1 type in your name: ")
  player2 = input("player 2 type in your name: ")
  print(player1, ":")
  word = input("type in your word: ")
  word = word.lower()
  word = word.replace(" ", "")
  #Users inputs data like the player mode, thier name and the the word they choose
  #(word)which gets turned to lowercase and has all its whitespaces deleted)
  w = Word(word)
  dictCheck = w.spellcheck()
  #spellchecks the word to make sure its real

  while dictCheck[0][1] != 1.0:
   print(word + " is not a valid word")
   word = input("type in your word: ")
   word = word.lower()
   word = word.replace(" ", "")
   w = Word(word)
   dictCheck = w.spellcheck()
 #if the the word is spellcheck correctly it return array with two vales with the last value([0][1]) suppose to be 1.0
#if  it doesnt equal 1.0
#it goes through a loop that will keep asking player 1 to type a word until the word is spellrd properly and proven to be
 #a real word
 elif menu=="One":
  dic=words
  random.shuffle(dic)
  word=dic[0]

  player2 = input("player 1 type in your name: ")
  player1=('CPU')
#if 1 player mode is choosen it shuffles/randomizes through the list that was created from the words in the text file
 #and then picks the first word in that list to be the word that player 1 has to guess
 if menu=="One" or "Two":
     break

print()
print()
print()
print()
print()
print()
print()
print()
print()
#prints a bunch of spaces so player 2 cant see the word player 1 choose/type
list = []
for i in range(len(word)):
    list.append(word[i])
spaces = []
for i in range(len(word)):
    spaces.append("-")
#Turns the choosen word to a list and creates a list filled with - and that is the same length as the choosen word

def hangword():
    hangman = "hang"
    if list != spaces:
        #checks if the list with - is equal to the list with the choosen word if it does it will print out plaer 2 has
        #won since they guessed all the letters in the word
        while hangman == "hang":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.hang()
                print(spaces)
                #checks if the guessword the user inputted is in the choosen word if it is
                #it goes through the for loop and checks where the guessword is located in the choosen word
                #then replaces the - in the space list in the same location it was located in the word
                # then it prints out the function from hangmanparts that corresponds with the hangmanbodypart your at
                #then it prints the space list
            else:
                hangmanparts.hanger()
                hangman = "hanger"
                print(spaces)
            if hangman == "hanger":
                break
            #else it prints out the next function from hangman parts , then the spaces  and then it sets hangman equal to
            #the next body part of hangman (in string from) so it breaks out of the loop in the current function and can
            #procced to the next function

#the procceding functions  follow simliar rules as the first

def hangerword():
    hangman = "hanger"
    if list != spaces:
        while hangman == "hanger":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.hanger()
                print(spaces)
            else:
                hangmanparts.head()
                hangman = "head"
                print(spaces)
            if hangman == "head":
                break


def headword():
    hangman = "head"
    if list != spaces:
        while hangman == "head":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.head()
                print(spaces)
            else:
                hangmanparts.body()
                hangman = "body"
                print(spaces)
            if hangman == "body":
                break


def bodyword():
    hangman = "body"
    if list != spaces:
        while hangman == "body":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.body()
                print(spaces)
            else:
                hangmanparts.onearm()
                hangman = "onearm"
                print(spaces)
            if hangman == "onearm":
                break


def onearmword():
    hangman = "onearm"
    if list != spaces:
        while hangman == "onearm":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.onearm()
                print(spaces)
            else:
                hangmanparts.twoarms()
                hangman = "twoarms"
                print(spaces)
            if hangman == "twoarms":
                break


def twoarmsword():
    hangman = "twoarms"
    if list != spaces:
        while hangman == "twoarms":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.twoarms()
                print(spaces)
            else:
                hangmanparts.oneleg()
                hangman = "oneleg"
                print(spaces)
            if hangman == "oneleg":
                break


def onelegword():
    hangman = "oneleg"
    if list != spaces:
        while hangman == "oneleg":
            if list == spaces:
                print(player2, "has won")
                break
            print(player2, ":")
            guessword = input("pick a letter: ")
            guessword = guessword.lower()
            if guessword in word:
                for i in range(len(word)):
                    if guessword == word[i]:
                        spaces[i] = guessword
                hangmanparts.oneleg()
                print(spaces)
            else:
                hangmanparts.twolegs()
                hangman = "twolegs"
                print(spaces)
            if hangman == "twolegs":
                print(player1, "has won")
                print("The word was",word)
                break
               #prints out player 1 won and the word if the whole hangman body prints out

def runhangman():
    hangword()
    hangerword()
    headword()
    bodyword()
    onearmword()
    twoarmsword()
    onelegword()


runhangman()
# runs all the functions in the hangman program