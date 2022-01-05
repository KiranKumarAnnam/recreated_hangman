from hangman_ascii import hangman_ascii, hangman_pics, words
import random

def call_hangman(guess_word):
    #print("Guessed word:", guess_word)
    def guess_format(counter=0):
        guess_list = []
        call_hangman_ascii()
        for each in range(len(guess_word)):
            guess_list.append('_')
        print(*guess_list)

        while counter < 7 :
            guess_achar = input("Guess a character in word : ")
            if guess_achar in guess_word and guess_achar not in guess_list:
                for each in range(len(guess_word)):
                    if guess_achar == guess_word[each]:
                        guess_list[each] = guess_word[each]
                print(" ")
                print("Guess list:", *guess_list)
                if ("".join(guess_list)) == guess_word:
                    counter = 0
                    break
            else:
                print(f"You still have {6 - counter} lives left")
                call_hangmanpic(counter)
                counter += 1
                print(" ")

        if counter:
            print("You have Lost a Life")
        else:
            print("You won!!")

    def call_hangman_ascii():
        print(*hangman_ascii)

    def call_hangmanpic(gc):
        print_hangman_pics = hangman_pics
        print(print_hangman_pics[gc])

    guess_format()

if __name__ == '__main__':
    guess_word = words[random.randint(0, len(words))]
    call_hangman(guess_word)
