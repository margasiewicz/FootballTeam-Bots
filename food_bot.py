from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from urls import food_hover, food_click, food_sleep_time

class FT_food_bot():
    def __init__(self):
        print('Po wybraniu posiłku otworzy się przeglądarka, zaloguj się na FT (masz na to 30s) i pozostaw ją włączoną')

    def choose_food(self):
        print('Wpisz numer posiłku i naciśnij Enter')
        print('1 - SMOOTHIE\n2 - BUŁKA\n3 - SCHABOWY')
        print('4 - SHAKE\n5 - KURCZAK Z RYŻEM\n6 - BIESIADA')
        choice = int(input())
        return choice

    def eat(self):
        choice = self.choose_food()
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--mute-audio")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get('https://game.footballteam.pl/food')
        sleep(30)
        
        while True:
            driver.get('https://game.footballteam.pl/food')
            sleep(5)
            try:
                hover = driver.find_element_by_xpath(food_hover.get(choice))
                ActionChains(driver).move_to_element(hover).perform()
                sleep(random.randint(2,5))
                driver.find_element_by_xpath(food_click.get(choice)).click()
                sleep(food_sleep_time.get(choice))
            except:
                sleep(3)
            
if __name__ == '__main__':
    bot = FT_food_bot()
    bot.eat()
