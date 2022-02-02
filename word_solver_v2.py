from datetime import date
from datetime import timedelta

wordlist = []
alphaScores = [ [0,"a"],[0,"b"],[0,"c"],[0,"d"],[0,"e"],[0,"f"],[0,"g"],[0,"h"],[0,"i"],[0,"j"],[0,"k"],[0,"l"],[0,"m"],[0,"n"],[0,"o"],[0,"p"],[0,"q"],[0,"r"],[0,"s"],[0,"t"],[0,"u"],[0,"v"],[0,"w"],[0,"x"],[0,"y"],[0,"z"] ]
Scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bestWords = [[0,""],[0,""],[0,""],[0,""],[0,""]]
numLetters = 0

def getWordList():
    global wordlist, numLetters
    numLetters = input("How many letters? ")
    if(numLetters == ""):
        numLetters = 5
    numLetters = int(numLetters)
    options = "1"
    if numLetters == 5:
        options = input("How would you like to play?\n\t1) Dictionary List\n\t2) Wordle Dictionary\n\t3) Wordle Solution Dictionary\n\t4) Get Specific Day's Word\n\t5) Get Today's Word\n>")
    if options == "1" and 2 <= numLetters <= 15:
        with open(f'./word_list/{numLetters}-letter-words.txt', 'r') as f:
            for line in f:
                wordlist.append(line.strip())
        print("\n")
        return
    elif options == "2":
        with open(f'./word_list/wordle_guess_list.txt', 'r') as f:
            for line in f:
                wordlist.append(line.strip())
        print("\n")
        return
    elif options == "3":
        with open(f'./word_list/wordle_solution_list.txt', 'r') as f:
            for line in f:
                wordlist.append(line.strip())
        print("\n")
        return
    elif options == "4":
        with open(f'./word_list/wordle_daily_list.txt', 'r') as f:
            for line in f:
                wordlist.append(line.strip())
        day = int(input ("\nWhich Day? "))
        print(wordlist[day % len(wordlist)])
        exit()
    elif options == "5":
        with open(f'./word_list/wordle_daily_list.txt', 'r') as f:
            for line in f:
                wordlist.append(line.strip())
        day = (date.today() - date(2021, 6, 19))
        print(wordlist[day.days % len(wordlist)])
        exit()
    print("Invalid number of letters: 2 - 15")
    exit()

def sortScore(e):
    return e[0]

def parseScores():
    global alphaScores,Scores
    alphaScores = [ [0,"a"],[0,"b"],[0,"c"],[0,"d"],[0,"e"],[0,"f"],[0,"g"],[0,"h"],[0,"i"],[0,"j"],[0,"k"],[0,"l"],[0,"m"],[0,"n"],[0,"o"],[0,"p"],[0,"q"],[0,"r"],[0,"s"],[0,"t"],[0,"u"],[0,"v"],[0,"w"],[0,"x"],[0,"y"],[0,"z"] ]
    for word in wordlist:
        for i in range(len(word)):
            val = ord(word[i])
            val -= 97
            alphaScores[val][0] += 1
    alphaScores.sort(key=sortScore)
    for i in range(26):
        Scores[ord(alphaScores[i][1])-97] = i

def addWord(word, score):
    global bestWords
    if score >= bestWords[0][0]:
        bestWords.remove(bestWords[0])
        bestWords.append([score,word])
        bestWords.sort(key=sortScore)

def clearWords():
    global bestWords
    bestWords = [[0,""],[0,""],[0,""],[0,""],[0,""]]

def findBestWords():
    clearWords()
    for word in wordlist:
        score = 0
        letters = []
        cancel = False
        for i in range(len(word)):
            if word[i] in letters:
                cancel = True
                break
            val = ord(word[i])
            val -= 97
            score += Scores[val]
            letters.append(word[i])
        if not cancel:
            addWord(word, score)
    #if less than 5 words available, include doubles
    if(bestWords[0][0] == 0):
        clearWords()
        for word in wordlist:
            score = 0
            for i in range(len(word)):
                val = ord(word[i])
                val -= 97
                score += Scores[val]
            addWord(word, score)


def printBestWords():
    for pair in bestWords:
        print(f'Word: {pair[1]}\tScore: {pair[0]}')

def printWordList():
    count = 0
    str = ""
    for word in wordlist:
        str += word
        count += numLetters + 1
        if count < 100:
            str += " "
        else:
            print(str)
            count = 0
            str = ""
    print(str)


def main():
    global wordlist

    #Init by telling them best words
    print("Best Starting Words & Scores:\n")
    printBestWords()
    print("\n")

    #keep looping
    while(True):
        #Enter Values
        known = "."
        while len(known) != numLetters and len(known) > 0:
            if(known != "."):
                print(f'Invalid String Size ({numLetters}): {known} = {len(known)}')
            known = input("Enter Known Leters and Place (**a**): ")
        unknown = input("Enter Known Letters in Unknown Places: ")
        nots = "."
        while len(nots) != numLetters and len(nots) > 0:
            if(nots != "."):
                print(f'Invalid String Size ({numLetters}): {nots} = {len(nots)}')
            nots = input("Enter wrong locations for Known Letters: ")
        cantBe = input("Enter Exiled Letters: ")
        print("")
        #Check all words remaining in the wordlist
        removeWords = []
        for line in wordlist:
            stop = False

            #Known Letters in Unknown Locations
            for i in range(len(unknown)):
                if not(unknown[i] in line):
                    stop = True
                    break
            if stop:
                removeWords.append(line)
                continue

            #Letters that can't be in the word
            for i in range(len(cantBe)):
                if cantBe[i] in line:
                    stop = True
                    break
            if stop:
                removeWords.append(line)
                continue

            #Known Letter Locations
            for i in range(len(known)):
                if known[i] == '*':
                    continue
                if line[i] != known[i]:
                    stop = True
                    break
            if stop:
                removeWords.append(line)
                continue
            
            #Known Letters in Wrong Spots
            for i in range(len(nots)):
                if nots[i] == '*':
                    continue
                if line[i] == nots[i]:
                    stop = True
                    break
            if stop:
                removeWords.append(line)
                continue

        #remove bad words
        for line in removeWords:
            wordlist.remove(line)

        #Print remaining Wordlist
        printWordList()
        print("\r\n")
        findBestWords()
        printBestWords()
        parseScores()
        print("\r\n")

if __name__ == "__main__":
    getWordList()
    parseScores()
    findBestWords()
    main()