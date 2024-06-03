from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
import config
import database
import datetime
import uuid

collection = database.connect_to_db()


def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy


def scrape():
    proxy_url = rand_proxy()
    profile = webdriver.FirefoxOptions()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy_url["host"])
    profile.set_preference("network.proxy.http_port", proxy_url["port"])
    profile.set_preference("network.proxy.ssl", proxy_url["host"])
    profile.set_preference("network.proxy.ssl_port", proxy_url["port"])
    driver = webdriver.Firefox(options=profile)
    driver.get('https://x.com/i/flow/login')

    sleep(8)
    username = driver.find_element(By.XPATH, "//input[@name='text']")
    username.send_keys("Suryanshhsharma")
    next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
    next_button.click()

    sleep(5)
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("Surya@123")
    next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
    next_button.click()

    sleep(5)
    trending = driver.find_elements(By.XPATH, "//div[@class='css-175oi2r r-6koalj r-1mmae3n r-3pj75a r-o7ynqc "
                                              "r-6416eg r-1ny4l3l r-1loqt21']")
    trending_titles = []
    for trend in trending:
        name = trend.find_elements(By.XPATH, ".//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3']")
        trending_titles.append(name[1].text)
    print(trending_titles)
    driver.quit()
    obj = {
        "unique_id": uuid.uuid4(),
        "ip": proxy_url["host"] + ':' + proxy_url["port"],
        "nameoftrend1": trending_titles[0],
        "nameoftrend2": trending_titles[1],
        "nameoftrend3": trending_titles[2],
        "nameoftrend4": trending_titles[3],
        "nameoftrend5": trending_titles[4],
        "date": datetime.datetime.now()
    }
    new = collection.insert_one(obj)
    return {
        "_id": str(new.inserted_id),
        "unique_id": str(obj["unique_id"]),
        "ip": proxy_url["host"] + ':' + proxy_url["port"],
        "nameoftrend1": trending_titles[0],
        "nameoftrend2": trending_titles[1],
        "nameoftrend3": trending_titles[2],
        "nameoftrend4": trending_titles[3],
        "nameoftrend5": trending_titles[4],
        "date": str(obj["date"])
    }

