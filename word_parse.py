
def main():
    with open("words_five.txt", 'w+') as o:
        with open("words_alpha.txt") as f:
            for line in f:
                if(len(line.strip())!=5):
                    continue
                else:
                    o.write(line)

if __name__ == '__main__':
    main()