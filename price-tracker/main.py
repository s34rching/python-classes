from bs4 import BeautifulSoup
import requests
import smtplib
import os

PRODUCT_URL = "https://www.amazon.com/Cuisinart-CPC-900-Multicooker-Pressure-Stainless/dp/B0813VGM8V/ref=pd_ci_mcx_pspc_dp_2_i_2?pd_rd_w=HBnwj&content-id=amzn1.sym.2dfc1605-9ad4-4767-b699-ffe3b61e0dc9&pf_rd_p=2dfc1605-9ad4-4767-b699-ffe3b61e0dc9&pf_rd_r=GT8K31QGMD3Q718C05JH&pd_rd_wg=YyYbo&pd_rd_r=d395bd27-fe46-4536-ae86-d3d4642f5bc4&pd_rd_i=B0813VGM8V"
PRICE_LIMIT = 150.01
FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36",
}

get_product_response = requests.get(PRODUCT_URL)
product_page_html = get_product_response.text

soup = BeautifulSoup(product_page_html, "html.parser")
price_element = soup.find(class_="a-offscreen")
title_element = soup.select_one("div#title_feature_div")

price_value = price_element.getText()
product_title = title_element.getText()
price = float(price_value.replace("$", "").strip())
product = product_title.strip()

if price < PRICE_LIMIT:
    with smtplib.SMTP("smtp.gmail.com") as client:
        client.starttls()
        client.login(user=FROM_EMAIL, password=PASSWORD)
        client.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert! Cheap {product}\n\n"
                f"The price is dropped below ${PRICE_LIMIT} for {product} and only ${price} now\n\n"
                f"Hurry up to get the thing:\n"
                f"{PRODUCT_URL}"
        )
