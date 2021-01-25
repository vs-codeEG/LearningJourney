import random

game_menu = ""

while game_menu != "exit":
    list_words = ['oda']
    chosen_word = random.choice(list_words)
    list_chosen_word = list(chosen_word)
    hints = list("-" * len(chosen_word))
    hints_word = "".join(hints)
    tries = 8
    mistakes = set()
    guess = set()

    print("H A N G M A N")
    game_menu = input("Type \"play\" to play the game, \"exit\" to quit: ")
    print()
    if game_menu == "play":

        while tries > 0 and hints_word != chosen_word:
            print(hints_word)
            letter = input('Input a letter: ')

            if letter == "" or (
                    len(letter) > 1 and letter.isupper() or ((not letter.isupper()) and len(letter) > 1)) or (
                    len(letter) > 1 and (not letter.isalpha())):
                print("You should input a single letter")
                print()

            if (letter.isupper() and len(letter) == 1) or ((not letter.isalpha()) and len(letter) == 1):
                print("Please enter a lowercase English letter")
                print()

            if letter.islower() and len(letter) == 1 and letter.isalpha():

                if letter in chosen_word:
                    if letter in guess:
                        print("You've already guessed this letter")

                    for x in range(len(hints_word)):
                        if letter == list_chosen_word[x]:
                            hints[x] = letter
                            hints_word = "".join(hints)
                            guess.update(letter)
                    print("")

                if letter not in chosen_word:
                    if letter in mistakes:
                        print("You've already guessed this letter")

                    if letter not in mistakes:
                        mistakes.update(letter)
                        tries -= 1
                        print("That letter doesn't appear in the word")

                    if tries == 0 and hints_word != chosen_word:
                        print("You lost!")
                        print("")
                        x = input("Type \"play\" to play the game, \"exit\" to quit: ")
                        game_menu = "exit"
                        break

                    print("")

            if hints_word == chosen_word:
                print(chosen_word)
                print("You guessed the word!")
                print("You survived!")
                print("")
                x = input("Type \"play\" to play the game, \"exit\" to quit: ")
                game_menu = "exit"
                break

    # elif hints_word == chosen_word or tries == 0:


    elif game_menu == "exit":
        break

    else:
        continue
