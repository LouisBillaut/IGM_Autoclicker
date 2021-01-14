from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from random import randint
from time import sleep

def init():
    """
    Return a List of all args in settings.txt file
    """
    args = []
    with open("settings.txt", "r") as reader:
        for line in reader:
            args.append(line)
    return args


def main():
    args = init()
    chromedriver_location = args[0]
    driver = webdriver.Chrome(chromedriver_location)
    #this link is the discord channel "emargement" of IGM server
    driver.get("https://discord.com/channels/688401448131624974/773863921206558761")

    while(True):
        try:
            wait = WebDriverWait(driver, 86400).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='reactionInner-15NvIl'][@aria-label='🙋, appuie pour réagir'][@aria-pressed='false'][@role='button']")))
            items = driver.find_elements_by_xpath("//div[@class='reactionInner-15NvIl'][@aria-label='🙋, appuie pour réagir'][@aria-pressed='false'][@role='button']")
            for i in items:
                #timer to be hide as a bot, can be removed if you want to be the first to sign
                #sleep(randint(1,5))
                i.click()
                print("signed in !")
        except ElementNotInteractableException:
            pass
        except (NoSuchElementException, ElementNotVisibleException):
            print("react button not found, check for the channel")
            quit()
        except TimeoutException:
            print("no call message made in 24h")
            quit()

if __name__ == '__main__':
    main()