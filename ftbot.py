from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


skill_hover = {
    "ofensywa": '//*[@id="container"]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]',
    "defensywa": '//*[@id="container"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]',
    "rozgrywanie:": '//*[@id="container"]/div/div[2]/div[1]/div[4]/div/div[2]/div[2]',
    "kondycja": '//*[@id="container"]/div/div[2]/div[1]/div[5]/div/div[2]/div[2]',
    "czytanie": '//*[@id="container"]/div/div[2]/div[1]/div[6]/div/div[2]/div[2]',
    "pressing": '//*[@id="container"]/div/div[2]/div[1]/div[7]/div/div[2]/div[2]',
    "stale_fragmenty": '//*[@id="container"]/div/div[2]/div[1]/div[8]/div/div[2]/div[2]',
    "skutecznosc": '//*[@id="container"]/div/div[2]/div[1]/div[9]/div/div[2]/div[2]'   
}
skill_btns = {
    "ofensywa": '//*[@id="container"]/div/div[2]/div[1]/div[2]/div/div[2]/button',
    "defensywa": '//*[@id="container"]/div/div[2]/div[1]/div[3]/div/div[2]/button',
    "rozgrywanie:": '//*[@id="container"]/div/div[2]/div[1]/div[4]/div/div[2]/button',
    "kondycja": '//*[@id="container"]/div/div[2]/div[1]/div[5]/div/div[2]/button',
    "czytanie": '//*[@id="container"]/div/div[2]/div[1]/div[6]/div/div[2]/button', 
    "pressing": '//*[@id="container"]/div/div[2]/div[1]/div[7]/div/div[2]/button',
    "stale_fragmenty": '//*[@id="container"]/div/div[2]/div[1]/div[8]/div/div[2]/button',
    "skutecznosc": '//*[@id="container"]/div/div[2]/div[1]/div[9]/div/div[2]/button',   
} 
spec_urls = {
    "ofensywa": "https://game.footballteam.pl/training/specialization/offensive",
    "defensywa": "https://game.footballteam.pl/training/specialization/defensive",
    "rozgrywanie": "https://game.footballteam.pl/training/specialization/playmaking",
    "kondycja": "https://game.footballteam.pl/training/specialization/condition",
    "czytanie": "https://game.footballteam.pl/training/specialization/reading",
    "pressing": "https://game.footballteam.pl/training/specialization/pressing",
    "stale_fragmenty": "https://game.footballteam.pl/training/specialization/freekicks",
    "skutecznosc": "https://game.footballteam.pl/training/specialization/efficacy"   
}
spec_hover = {
    "jeden": '//*[@id="container"]/div/div[2]/div/div[2]/div[2]/div[2]',
    "dwa": '//*[@id="container"]/div/div[2]/div/div[3]/div[2]/div[2]',
    "trzy": '//*[@id="container"]/div/div[2]/div/div[4]/div[2]/div[2]',
    "cztery": '//*[@id="container"]/div/div[2]/div/div[5]/div[2]/div[2]'
}
specka_btns = {
    "jeden": '//*[@id="container"]/div/div[2]/div/div[2]/div[2]/button',
    "dwa": '//*[@id="container"]/div/div[2]/div/div[3]/div[2]/button',
    "trzy": '//*[@id="container"]/div/div[2]/div/div[4]/div[2]/button',
    "cztery": '//*[@id="container"]/div/div[2]/div/div[5]/div[2]/button'
    
}
other_btns = {
    "first_login_btn": '//*[@id="buttons"]/div/button[1]',
    "login_screen": '//*[@id="modal-login-tab"]/h5',
    "put_login": '//*[@id="login-form"]/div[1]/input',
    "put_pass": '//*[@id="login-form"]/div[2]/input',
    "login_btn": '//*[@id="btn-login"]'
}


class FT_training_bot:
    def __init__(self):
        
        print("Witaj! Wybierz parametry, a po otwarciu okna przeglądarki zaloguj się na swoje konto\n\n")

    def pick_training(self): 

        print("Chcesz trenować specjalizację czy zwykłe umiejętności?")
        print("1 - specjalizacja\n2 - zwykła umiejętność")
        training_choice = int(input())
        if training_choice not in [1,2]:
            print ('Wybierz poprawną opcję')
            return self.pick_training()
        else:
            return training_choice

    def choose_parameters(self, spec_or_skill_choice):

        print('Ile chcesz zrobić treningów?')
        energy = int(input())
        print('Wpisz czas trwania jednego treningu w sekundach')
        delay = int(input())
        
        if spec_or_skill_choice == 1:
            # 1 for specialization
            # 2 for basic skill
            print("wybierz specjalizację do trenowania i naciśnij enter:")
            print("1 - ofensywa\n2 - defensywa\n3 - rozgrywanie\n4 - kondycja\n5 - czytanie gry\n6 - pressing\n7 - stałe fragmenty\n8 - skuteczność")
            spec = int(input())
            print("Wybierz który skill ze specjalizacji chcesz trenować i naciśniej enter:")
            print("1 - pierwszy\n2 - drugi\n3 - trzeci\n4 - czwarty")
            print("Wybierz PIERWSZY skill:")
            skill1 = int(input())
            print("Wybierz DRUGI skill:")
            skill2 = int(input())
            spec_url = list(sp_urls.items())[skill-1][1]        
        else:
            print("\nWybierz umiejętność do trenowania i naciśnij enter")
            print("1 - ofensywa\n2 - defensywa\n3 - rozgrywanie\n4 - kondycja\n5 - czytanie gry\n6 - pressing\n7 - stałe fragmenty\n8 - skuteczność")
            print("Wybierz PIERWSZĄ umiejętność:")
            skill1 = int(input())
            print("Wybierz DRUGĄ umiejętność:")
            skill2 = int(input())
            hover1 = list(skill_hover.items())[skill1-1][1]
            button1 = list(skill_btns.items())[skill1-1][1]
            hover2 = list(skill_hover.items())[skill2-1][1]
            button2 = list(skill_btns.items())[skill2-1][1]
            spec_url = 'https://game.footballteam.pl/training'

            if (skill1 == skill2):
                energy = energy*2

        parameters = {
            'energy': energy,
            'delay': delay,
            'spec_url': spec_url,
            'hover1': hover1,
            'button1': button1,
            'hover2': hover2,
            'button2': button2
        }
        return parameters
        
    def training(self, parameters):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--mute-audio")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://game.footballteam.pl/")
        sleep(30)

        self.driver.get(parameters.get('spec_url'))
        sleep(5)
        hover1 = self.driver.find_element_by_xpath(parameters.get('hover1'))
        hover2 = self.driver.find_element_by_xpath(parameters.get('hover2'))
        for x in range(parameters.get('energy')//2):
            for y in range(2):
                ActionChains(self.driver).move_to_element(hover1).perform()
                sleep(2)
                try:
                    self.driver.find_element_by_xpath(parameters.get('button1')).click()
                except:
                    pass
                ActionChains(self.driver).move_to_element(hover2).perform()
                sleep(2)
                try:
                    self.driver.find_element_by_xpath(parameters.get('button2')).click()
                except:
                    pass
            if(x%20==0 and x!=0):
                print("Spalilem okolo "+str(2*x)+" energii")
            sleep(parameters.get('delay'))
        
        self.driver.quit()

if __name__ == '__main__':
    bot = FT_training_bot()
    training_choice = bot.pick_training()
    parameters = bot.choose_parameters(training_choice)
    bot.training(parameters)

    