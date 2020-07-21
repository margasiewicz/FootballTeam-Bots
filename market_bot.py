

class FTBot:
    def __init__(self):
        print("Witaj! Wybierz parametry, a po otwarciu okna przeglądarki zaloguj się na swoje konto\n\n")

    
    def refreshtoggle(self, color):
        sleep(2)
        self.driver.get("https://game.footballteam.pl/market")
        sleep(3)
        self.driver.find_element_by_xpath\
                (market.get("toggle_item_color"))\
                .click()
        sleep(2)
        self.driver.find_element_by_xpath\
            (rynek.get(color))\
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

        'TODO: make following more readable'
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
        
    def market_start(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--mute-audio")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://game.footballteam.pl/")
        sleep(30)
        
