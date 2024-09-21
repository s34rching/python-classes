from datetime import datetime
import requests
import os

BASE_URL = "https://trackapi.nutritionix.com"
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")

NUTRITIONIX_EXERCISES_ENDPOINT = f"{BASE_URL}/v2/natural/exercise"

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")


def get_exercise_payload(exercise):
    now = datetime.now()

    return {
        "sheet1": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


nutritionix_headers = {
    "Content-Type": 'application/json',
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"
}

user_data = input("What exercises have you completed for today?: ")

query_params = {
    "query": user_data
}

nutritionix_response = requests.post(NUTRITIONIX_EXERCISES_ENDPOINT, json=query_params, headers=nutritionix_headers)
nutritionix_data = nutritionix_response.json()
exercises_data = nutritionix_data["exercises"]

exercise_payloads = [get_exercise_payload(exercise) for exercise in exercises_data]

for payload in exercise_payloads:
    sheety_headers = {
        "Authorization": SHEETY_AUTH_TOKEN
    }

    sheety_response = requests.post(SHEETY_ENDPOINT, json=payload, headers=sheety_headers)
    print(sheety_response.json())
