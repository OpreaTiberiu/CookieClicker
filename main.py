from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BUFF_COOLDOWN = 5

GAME_DURATION = 300


def get_buffs():
    store_elements = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    buffs = []
    for element in store_elements:
        if element.text and "-" in element.text:
            text = element.text
            price_string = text.split("-")[1].split()[0].strip()
            price = int(price_string.replace(",", ""))
            buff = {"element": element, "price": price}
            buffs.append(buff)

    return buffs[::-1]


driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(value="cookie")

time_start = time.time()

timeout = time_start + BUFF_COOLDOWN

while True:  #(int(time.time() - time_start)) <= GAME_DURATION:
    cookie.click()
    if time.time() >= timeout:
        money = int(driver.find_element(value="money").text.replace(",", ""))
        for buff in get_buffs():
            if money >= buff["price"]:
                buff["element"].click()
                break
        timeout = timeout + BUFF_COOLDOWN
