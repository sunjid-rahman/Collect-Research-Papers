from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
import os
from urllib.parse import urlparse
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import zipfile
from pathlib import Path
import shutil
from datetime import datetime

article_dic = {}


def collect(driver, article_path, limit):
    size = 0
    try:
        elements = driver.find_elements_by_tag_name("a")
        for element in elements:
            try:
                article_url = element.get_attribute("href")
                if article_url.endswith(".pdf"):
                    article_data = requests.get(article_url).content
                    a = urlparse(article_url)
                    file = os.path.basename(a.path)
                    local_filename = str(article_path) + '\\' + file
                    if len(article_dic) < limit:
                        if local_filename not in article_dic:
                            print(article_url)
                            article_dic[local_filename] = article_data
                            size += 1
            except:
                pass
    except:
        pass
    return size


def collect_articles(search_key=None, limit=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    driver.get("https://scholar.google.com/")
    driver.maximize_window()
    collected_article = 0
    q = driver.find_element_by_xpath("//input[@name='q']")
    q.send_keys(search_key)
    q.send_keys(Keys.ENTER)
    time.sleep(50)
    article_path = f"{search_key}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    for i in range(limit):
        size = collect(driver, article_path, limit)
        collected_article = collected_article + size
        print(collected_article)
        if collected_article >= limit:
            break
        else:
            next = driver.find_element_by_xpath("/html/body/div/div[10]/div[2]/div[3]/div[3]/div[2]/center/table/tbody/tr/td[12]/a")
            next.click()
    os.mkdir(article_path)
    for key, value in article_dic.items():
        try:
            with open(key, 'wb') as f:
                # data = requests.get(value).content
                f.write(value)
        except:
            pass

    driver.quit()