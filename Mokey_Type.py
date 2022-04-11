
from selenium import webdriver
import time
import pyautogui
import random

tex = "sdlyfg"

driver = webdriver.Firefox()

driver.get("https://monkeytype.com/")
i = 1
j = 1
time.sleep(10)

s = ""
sj = 1

for k in range(10000):

    for u in range(140):
        try:
            if sj != j:
                sj = j
                s += " "

            s += driver.find_element_by_xpath("/html/body/div[35]/div/div[2]/div[2]/div[1]/div[7]/div[3]/div["+str(j)+"]/letter["+str(i)+"]").text
            i += 1

        except:
            j += 1
            i = 1
    for o in s:
        pyautogui.typewrite(o)
        time.sleep(random.randrange(10)/50)
    for o in range(random.randrange(3)):
        pyautogui.typewrite(tex[random.randrange(5)])

    s = ""

    k = 0
    while True:
        k += 1
        if i < 1:
            j -= 1
            i = 15
        try:

            if driver.find_element_by_xpath("/html/body/div[35]/div/div[2]/div[2]/div[1]/div[7]/div[3]/div["+str(j)+"]/letter["+str(i)+"]").get_attribute("class") != "":
                break

        except:

            i -= 1
            continue
        i -= 1

    if k > 10:
        s += " "
        j += 1
        i = 1

