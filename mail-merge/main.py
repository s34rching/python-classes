def mail_merger():
    with open("./mail-merge/Input/Letters/starting_letter.txt", mode="r") as template_file:
        template = template_file.read()

    with open("./mail-merge/Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()

    for name in names:
        refined_name = name.strip()

        letter_content = template.replace("[name]", refined_name)

        with open(f"./mail-merge/Output/ReadyToSend/letter-for-{refined_name}.docx", mode="w") as letter_file:
            letter_file.write(letter_content)


mail_merger()
