from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from urls import work_hover, work_click, work_sleep_time

class FT_training_bot:
    def __init__(self):
        print('Po wybraniu pracy otworzy się przeglądarka, zaloguj się na FT (masz na to 30s) i pozostaw ją włączoną')

    def pick_parameters(self):
        print('Wpisz numer pracy i naciśnij Enter')
        print('1 - RĘCZNIKOWY\n2 - MASKOTKA\n3 - EKSPERT W STUDIO')
        print('4 - NOSIWODA\n5 - TRENER MŁODZIKÓW\n6 - WYSTĘP W REKLAMIE')
        print('7 - PODAWACZ PIŁEK\n8 - KOMENTATOR\n9 - WYSTĘP W TURNIEJU GWIAZD')
        choice = int(input())
        return choice

    def work(self):
        choice = self.pick_parameters()

        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--mute-audio")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get('https://game.footballteam.pl/work/')
        sleep(30)
        driver = webdriver.Chrome()
        while True:
            driver.get('https://game.footballteam.pl/work/')
            sleep(5)
            try:
                hover = driver.find_element_by_xpath(work_hover.get(choice))
                ActionChains(driver).move_to_element(hover).perform()
                sleep(random.randint(2,5))
                driver.find_element_by_xpath(work_click.get(choice)).click()
                sleep(work_sleep_time.get(choice))
            except:
                sleep(3)

if __name__ == '__main__':
    bot = FT_training_bot()
    bot.work()