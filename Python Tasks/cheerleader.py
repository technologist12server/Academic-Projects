# store my favorite word
favorite_word = "XHOSA"

# ask the user to enter the word
name_input = input("Enter Your favorite word: ").upper()

# check if the user entered the correct word
if name_input == favorite_word:

    # cheer for each letter
    for letter in favorite_word:

        vowel_check = 'an' if letter in 'AEIOU' else 'a'
        print(f"Give me a {vowel_check} {letter}!")

    print(f"What does it say????? {favorite_word}!!!!!!")

else:
    print("Error: Incorrect word entered. Please try again.")
