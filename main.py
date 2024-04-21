import time
import random
import string
from pystyle import Colors, Colorate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tmail import *
import undetected_chromedriver as uc

def save_acc(emailpass):
    with open('acc.txt', 'a') as file:
        file.write(emailpass + '\n')

def gen():
    email = get_temp_mail()

    def generate_random_nickname(length=8):
        characters = string.ascii_letters + string.digits
        random_nickname = ''.join(random.choice(characters) for _ in range(length))
        return random_nickname

    def generate_random_password(length=8):
        characters = string.ascii_letters + string.digits + "_-=+$"
        random_password = random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice("_-=+$")
        random_password += ''.join(random.choice(characters) for _ in range(length - 3))
        random_password_list = list(random_password)
        random.shuffle(random_password_list)
        random_password = '_A'.join(random_password_list)

        return random_password

    random_password = generate_random_password()

    browser = uc.Chrome(headless=True, se_subprocess=False)
    wait = WebDriverWait(browser, 10)

    print(Colors.red + f"[ ! ] Creating account")
    if email:
        try:
            print(Colors.light_green + f"[ ! ] Created temp mail: {email}")
            nickname = generate_random_nickname()
            print(Colors.light_green + f"[ ! ] Nickname: {nickname}")
            browser.get("https://cristalix.gg/register")
            browser.set_window_size(1552, 832)
            browser.find_element(By.ID, "username-input").click()
            browser.find_element(By.ID, "username-input").send_keys(nickname)
            browser.find_element(By.ID, "email-input").click()
            browser.find_element(By.ID, "email-input").send_keys(email)
            browser.find_element(By.ID, "password-input").click()
            browser.find_element(By.ID, "password-input").send_keys(random_password)
            print(Colors.light_green + f"[ ! ] Password: {random_password}")
            browser.find_element(By.ID, "repeat-password-input").click()
            browser.find_element(By.ID, "repeat-password-input").send_keys(random_password)
            browser.find_element(By.ID, "mojang-username-input").click()
            browser.find_element(By.ID, "mojang-username-input").send_keys("gdeVanezus")
            confch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span:nth-child(2)")))
            browser.execute_script("arguments[0].click();", confch)
            button = wait.until(EC.element_to_be_clickable((By.ID, "register-button")))
            browser.execute_script("arguments[0].scrollIntoView(true);", button)
            button.click()
            time.sleep(10)
            idmsg = get_id(email)
            if idmsg is None:
                raise Exception("Err, message id")
            xd = get_mail_url(email, idmsg)
            if xd is None:
                raise Exception("Err, mail url")
            print(Colors.light_green + f"[ X ] Confirm url: {xd}")
            browser.get(xd)
            lpass = f"{email}:{random_password}"
            print(Colorate.Horizontal(Colors.rainbow, f"[ X ] Created new acc: {lpass}", 1))
            save_acc(lpass)
            browser.close()
            gen()

        except Exception as e:
            print(Colors.red + f"[ ! ] Error")
            browser.close()
            gen()

def main():
    print(Colorate.Horizontal(Colors.yellow_to_red, "Cristalix autoreg v1", 1))
    print(Colorate.Horizontal(Colors.rainbow, "[ X ] Starting", 1))
    gen()

if __name__ == "__main__":
    main()
