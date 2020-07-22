from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from urls import market_btns

class FT_market_bot:
    def __init__(self):
        print("Witaj! Wybierz parametry, a po otwarciu okna przeglądarki zaloguj się na swoje konto\n\n")

    def refreshtoggle(self, color):
        sleep(2)
        self.driver.get("https://game.footballteam.pl/market")
        sleep(3)
        #find given color category and click it
        self.driver.find_element_by_xpath\
                (market_btns.get("toggle_item_color"))\
                .click()
        sleep(2)
        self.driver.find_element_by_xpath\
            (market_btns.get(color))\
            .click() 
        sleep(3)
    def refresh(self):
        sleep(2)
        self.driver.get("https://game.footballteam.pl/market")
        sleep(3)
    def pick_parameters(self):
        print('Jaki kolor itemu chcesz kupić?')
        print("1 - złote\n2 - czerwone\n3 - zielone")
        print("4 - niebieskie\n5 - szare\n6 - jakikolwiek")

        '''
        TODO: make following more readable
        '''
        color = int(input())
        colors = ['gold', 'red', 'green', 'blue', 'grey', 'any']
        color = colors[color-1]

        print('Po jakiej cenie maksymalnie chcesz kupować?')
        price = int(input())
        print('Ile przedmiotów chcesz kupić?')
        qty = int(input())

        parameters = {
            'color':color,
            'price':price,
            'qty':qty
        }
        return parameters

    def market_start(self, parameters):
            color = parameters.get('color')
            price = parameters.get('price')
            qty = parameters.get('qty')

            options = webdriver.ChromeOptions()
            #options.add_argument('--headless')
            options.add_argument("--mute-audio")
            options.add_argument('--ignore-certificate-errors-spki-list')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(options=options)
            self.driver.get("https://game.footballteam.pl/")
            sleep(30)
            self.refreshtoggle(color)


            while qty>0:
                try:      
                    #sort min to max price
                    self.driver.find_element_by_xpath\
                        (market_btns.get('min-max')).click()
                    sleep(1)
                    #find min price and compare it to given min price
                    min_price = self.driver.find_element_by_xpath\
                        (market_btns.get('first_item')).text
                    min_price = int(min_price)
                    if min_price<=price:
                        print('próbuję kupić po cenie', min_price)
                        self.driver.find_element_by_xpath\
                        (market_btns.get("buy"))\
                        .click()
                        self.driver.find_element_by_xpath\
                        (market_btns.get("confirm"))\
                        .click()
                        qty-=1
                            
                except:
                        self.refresh()


if __name__ == '__main__':
    bot = FT_market_bot()
    parameters = bot.pick_parameters()
    bot.market_start(parameters)