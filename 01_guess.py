import random

def main():
    five_letter_words = ["pizza", "later", "solar", "quark", "proof", "quake"]
    chosen_word = five_letter_words[random.randint(0, 5)]
    print("The unknown word begins with a {}".format(chosen_word[0].upper()))

    guesses_left = 10
    correct_guess = False
    while(guesses_left and not(correct_guess)):
        current_guess = input("GUESS: ").lower()
        if current_guess == "":
            print("You wasted a guess!")
            guesses_left -= 1
        elif len(current_guess) != 5:
            print ("0, 1, 2, 3, 4 that's how we count to five!")
            guesses_left -= 1
        elif current_guess[0] != chosen_word[0]:
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif current_guess != chosen_word:
            guesses_left -= 1
            print("You have {} guesses left".format(guesses_left))
        else:
            print("Good Job! You are one with the Source.")
            correct_guess = True

main()