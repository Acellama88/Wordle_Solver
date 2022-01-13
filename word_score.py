scores = [8392, 2089, 2744, 2811, 7800, 1238, 1971, 2284, 5067, 376, 1743, 4246, 2494, 4043, 5219, 2299, 139, 5143, 6537, 4189, 3361, 878, 1171, 361, 2521, 474]
words = [ [0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""],[0,""] ]

def sortScores():
    sortScores = scores.copy()
    sortScores.sort()
    retVal = scores.copy()
    for i in range(26):
        for j in range(26):
            if retVal[j] == sortScores[i]:
                retVal[j] = i
                break
    print(retVal)
    return retVal

def sortFunc(e):
    return e[0]

def addWord(word, score):
    global words
    if score >= words[0][0]:
        words.remove(words[0])
        words.append([score,word])
        words.sort(key=sortFunc)

def main():
    points = sortScores()
    with open("words_five.txt", 'r') as f:
        for line in f:
            score = 0
            letters = []
            cancel = False
            for i in range(len(line.strip())):
                if line[i] in letters:
                    cancel = True
                    break
                val = ord(line[i])
                val -= 97
                score += points[val]
                letters.append(line[i])
            if not cancel:
                addWord(line, score)
    print(words)

if __name__ == '__main__':
    main()