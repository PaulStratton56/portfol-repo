from random import *

#WORDINC - Purpose: Test your vocab skills by being given a part of a word and being asked to give a word containing that part!

#Getting words from words.txt
words = open("words.txt","r")
wordList = words.readlines()
for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

#Input maximum number of tries and begin a used word list
maxTries = int(input("Max tries: "))
usedWords = []

#Testing to see if the word passes the test (Is it a word? Is the given part in the word?)
def testWord(word,part):
    global usedWords
    if word == "":
        return False
    elif (word in wordList) and (part in word) and (word not in usedWords):
        usedWords.append(word)
        return True
    elif word in usedWords:
        print("You've already used "+'"'+word+'".')
    elif word not in wordList:
        print('"'+word+'"' + " is not a recognized word.")
    else:
        print('"'+part+'"'+ " is not in " + word + ".")
        return False

#Main loop =====
while True:
    #Establish a part, reset the try count, etc.
    tries = 0
    randWord = wordList[randint(0,len(wordList)-1)]
    while len(randWord) < 5:
        randWord = wordList[randint(0,len(wordList)-1)]
    randStart = randint(0,len(randWord)-4)
    part = randWord[randStart:min((randStart + randint(2,3)),len(randWord)-1)]
    givenWord = ""

    #While you're failing to give the right word:
    while not testWord(givenWord,part):
        #If you've gone over the limit you set, it gives you a word then moves on.
        if tries >= maxTries:
            print("Example word: " + randWord)
            break
        #If you haven't gone over the limit, you have a chance to put in a word!
        else:
            tries+=1
            givenWord = input("Word with " + part + ": ").lower()
