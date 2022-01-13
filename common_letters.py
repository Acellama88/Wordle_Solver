alpha = "abcdefghijklmnopqrstuvwxyz"
occurance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def main():
    with open("words_five.txt", 'r') as f:
        for line in f:
            for i in range(len(line.strip())):
                val = ord(line[i])
                val -= 97
                occurance[val] += 1
    for i in range(len(alpha)):
        print(f"{alpha[i]} = {occurance[i]}")
    print(occurance)

if __name__ == '__main__':
    main()