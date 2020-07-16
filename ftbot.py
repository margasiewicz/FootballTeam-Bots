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
        else:
            print("\nWybierz umiejętność do trenowania i naciśnij enter")
            print("1 - ofensywa\n2 - defensywa\n3 - rozgrywanie\n4 - kondycja\n5 - czytanie gry\n6 - pressing\n7 - stałe fragmenty\n8 - skuteczność")
            print("Wybierz PIERWSZĄ umiejętność:")
            skill1 = int(input())
            print("Wybierz DRUGĄ umiejętność:")
            skill2 = int(input())
            hover1 = list(skill_hover.items())[skill1-1][0]
            button1 = list(skill_btns.items())[skill1-1][0]
            hover2 = list(skill_hover.items())[skill2-1][0]
            button2 = list(skill_btns.items())[skill2-1][0]

            if (skill1 == skill2):
                ile_energii = ile_energii*2
        parameters = {
            'energy': energy,
            'delay': delay,
            'hover1': hover1,
            'button1': button1,
            'hover2': hover2,
            'button2': button2
        }
        return parameters
        




if __name__ == '__main__':
    bot = FT_training_bot()
    training_choice = bot.pick_training()
