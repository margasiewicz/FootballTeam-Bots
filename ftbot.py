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
    def pick_training(self):
        print("Welcone to training bot. Pick parameters and log in to your account after\
        browser opens\n\n")

        print("Do you wish to train specialization or basic skill?")
        print("1 - spacialization\n2 - basic skill")
        training_choice = int(input())




if __name__ == '__main__':
    bot = FT_training_bot()