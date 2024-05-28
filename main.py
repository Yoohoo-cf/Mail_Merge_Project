# Transfer names file to names list for usage
with open("./Input/Names/invited_names.txt") as name_f:
    invited_names = name_f.readlines()
    # print(invited_names)

with open("./Input/Letters/starting_letter.txt") as letter_f:
    starting_letter = letter_f.read()

for name in invited_names:
    new_name = name.strip()

    # Replace "[name]" in starting_letter with each of invited names
    inviting_letter = starting_letter.replace("[name]", new_name)

    # writing the inviting_letter to ReadyToSend directory
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(inviting_letter)




