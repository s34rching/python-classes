from datetime import datetime, timedelta
import requests
import os

BASE_URL = "https://pixe.la/v1/users"
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID")
TZ = os.environ.get("TZ_DATABASE_NAME")

CREATE_GRAPH_ENDPOINT = f"{BASE_URL}/{PIXELA_USERNAME}/graphs"
ADD_PIXEL_ENDPOINT = f"{BASE_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"

auth_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


def get_formatted_date(days_ago):
    target_date = datetime.now() - timedelta(days=days_ago)
    return target_date.strftime("%Y%m%d")


def add_pixels(quantity: str, days_ago: int = 0):
    date = get_formatted_date(days_ago)

    add_pixel_params = {
        "date": date,
        "quantity": quantity
    }

    add_pixel_response = requests.post(ADD_PIXEL_ENDPOINT, json=add_pixel_params, headers=auth_headers)
    print(add_pixel_response.json())


def update_pixels(quantity: str, days_ago: int):
    date = get_formatted_date(days_ago)

    update_pixel_params = {
        "quantity": quantity
    }

    update_pixel_endpoint = f"{ADD_PIXEL_ENDPOINT}/{date}"
    update_pixel_response = requests.put(update_pixel_endpoint, json=update_pixel_params, headers=auth_headers)
    print(update_pixel_response.json())


def delete_pixels(days_ago: int):
    date = get_formatted_date(days_ago)

    delete_pixel_endpoint = f"{ADD_PIXEL_ENDPOINT}/{date}"
    delete_pixel_response = requests.delete(delete_pixel_endpoint, headers=auth_headers)
    print(delete_pixel_response.json())


completed_tasks = input("How many tasks have you completed today?: ")
add_pixels(completed_tasks)

