from art import logo, vs
from data import data
import random
import os

def show_entity(option, person_data):
    print(f"{option}: {person_data["name"]}, {person_data["description"]} from {person_data["country"]}")


def get_unique_entity(person_data=None, previous_person=None):
    random_person = random.choice(data)

    if person_data == None:
        return random_person
    else:
        if (random_person["name"] == person_data["name"]) or (random_person["name"] == person_data["name"]):
            get_unique_entity()
        else:
            return random_person


def check_answer(entity_a, entity_b, user_guess):
    if (entity_a["follower_count"] > entity_b["follower_count"]):
        return user_guess == 'A'
    return user_guess == 'B'


def higher_lower():
    user_score = 0
    person_a = get_unique_entity()
    previous_person = None

    print(logo)

    is_correct = True
    while is_correct:
        person_b = get_unique_entity(person_a, previous_person)

        show_entity("Compare A", person_a)
        print(vs)
        show_entity("Against B", person_b)

        user_guess = input("Try to guess who has more Instagram followers. A or B?: ").upper()

        is_correct = check_answer(person_a, person_b, user_guess)

        if is_correct:
            user_score += 1
            previous_person = person_a
            person_a = person_b
            os.system("clear")
            print(f"Well done. Your score is {user_score}")
        else:
            print(f"\nUnfortunately. Game is over. Your score is {user_score}\n")


higher_lower()