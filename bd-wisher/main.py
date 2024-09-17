import pandas
import datetime
import random
import smtplib
import os

FROM_EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
LETTER_PATTERNS = [1, 2, 3]
now = datetime.datetime.now()

birthdays_data = pandas.read_csv("./bd-wisher/birthdays.csv")

for (_, member_birthday) in birthdays_data.iterrows():
    if now.month == member_birthday["month"] and now.day == member_birthday["day"]:
        chosen_pattern = random.choice(LETTER_PATTERNS)

        with open(f"./bd-wisher/letter_templates/letter_{chosen_pattern}.txt", mode="r") as letter_file:
            letter_content = letter_file.read()
            named_content = letter_content.replace("[NAME]", member_birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as client:
            client.starttls()
            client.login(user=FROM_EMAIL, password=PASSWORD)
            client.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=member_birthday["email"],
                msg=f"Subject:Happy Birthday\n\n{named_content}"
            )
