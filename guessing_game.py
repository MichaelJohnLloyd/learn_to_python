prime_word = "Welcome"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False


while guess != prime_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose!")
else:
    print("You Win!")