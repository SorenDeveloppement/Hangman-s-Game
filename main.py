import random


def game(wordToFind: str):
    after: str = ""
    already: str = ""

    run: bool = True
    after = "_" * (len(wordToFind) - 1)

    print("Pendu. Trouvez le bon mot !")
    while run:
        print(after.find("_"))
        print(after, wordToFind, after == wordToFind)
        aword: list = []
        letter: str = input("Proposez une lettre : ")
        if not (letter in already):
            if letter in wordToFind:
                for i in range(0, len(wordToFind) - 1):
                    if letter == wordToFind[i]:
                        aword.append(letter)
                    else:
                        aword.append(after[i])
                after = ''.join(aword)
                print(after)
                if after.find("_") == -1:
                    print("Vous avez gagné !\n")
                    run = False
            else:
                print("Cette lettre n'est pas dans le mot !")
        else:
            print("Lettre déjà proposée !")

        already += letter


while True:
    word = None
    with open("dic.txt", 'r') as f:
        lines = f.readlines()
        rdm = random.randint(0, len(lines))
        print(len(lines))
        for i, line in enumerate(lines):
            if i == rdm:
                print(i, line)
                word = line.lower()

    game(word)
