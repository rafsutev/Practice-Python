# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

def check_word(length,letter):

    with open("SOWPODS dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()

            if len(word) <= length and word[0] == letter:
                print(word)

user_length = int(input("What is the length of your desired word? "))

user_starting_letter = str(input("What letter does your word start with? ").upper())

check_word(user_length, user_starting_letter)

