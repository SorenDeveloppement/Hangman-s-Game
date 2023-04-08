import random

words: list = ["banane", "coco", "amende"]
after: str = ""
already: str = ""


def game(word: str):
    global after
    global already

    run: bool = True
    after = "_" * len(word)

    print("Pendu. Trouvez le bon mot !")
    while run:
        aword: list = []
        letter: str = input("Proposez une lettre : ")
        if not (letter in already):
            if letter in word:
                for i in range(len(word)):
                    if letter == word[i]:
                        aword.append(letter)
                    else:
                        aword.append(after[i])
                after = ''.join(aword)
                print(after)
                if word == after:
                    print("Vous avez gagné !\n")
                    run = False
            else:
                print("Cette lettre n'est pas dans le mot !")
        else:
            print("Lettre déjà proposée !")

        already += letter


while True:
    game(words[random.randint(0, len(words) - 1)])
