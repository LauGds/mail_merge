PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    guess_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for guess in guess_list:
        new_name = guess.strip()
        final = content.replace(PLACEHOLDER, new_name)
        print(final)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as save_letter:
            save_letter.write(final)
