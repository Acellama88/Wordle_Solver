scores = [25, 9, 14, 15, 24, 6, 8, 10, 20, 2, 7, 19, 12, 17, 22, 11, 0, 21, 23, 18, 16, 4, 
5, 1, 13, 3]

def main():
    while(True):
        known = ""
        while len(known) != 5:
            known = input("Enter known string with * as unknown: ")
        unknown = input("Enter characters in string but unknown location: ")
        cantBe = input("Enter characters that can't be in the word: ")
        nots = "*****"
        notIts = []
        while len(nots) == 5:
            notIts.append(nots.strip())
            nots = input("Enter string where a character can't be (*'s unknown): ")
        notIts.remove("*****")
        finalWords = []
        print("Running... \r\n")
        with open("words_five.txt", 'r') as f:
            for line in f:
                stop = False
                for i in range(len(unknown)):
                    if not(unknown[i] in line):
                        stop = True
                        break
                for i in range(len(cantBe)):
                    if cantBe[i] in line:
                        stop = True
                        break
                if stop:
                    continue
                for i in range(5):
                    if known[i] == '*':
                        continue
                    if line[i] != known[i]:
                        stop = True
                        break
                if stop:
                    continue
                for j in range(len(notIts)):
                    for i in range(5):
                        if notIts[j][i] == '*':
                            continue
                        if line[i] == notIts[j][i]:
                            stop = True
                            break
                    if stop:
                        break
                if stop:
                    continue
                finalWords.append(line.strip())
            print(finalWords)
        print("\r\n")
        bestWord = [0, "     "]
        for j in range(len(finalWords)):
            score = 0
            letters = []
            cancel = False
            for i in range(len(finalWords[j])):
                if finalWords[j][i] in letters:
                    cancel = True
                    break
                val = ord(finalWords[j][i])
                val -= 97
                score += scores[val]
                letters.append(finalWords[j][i])
            if not cancel:
                if bestWord[0] < score:
                    bestWord = [score, finalWords[j]]
        print(f"Best next guess is: {bestWord[1]}")
        print("\r\n")
        exit = input("Exit? ")
        if exit[0] == 'y' or exit[0] == 'Y':
            break
        print("\r\n")


if __name__ == "__main__":
    main()