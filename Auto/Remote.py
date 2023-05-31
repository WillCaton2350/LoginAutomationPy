from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver import Keys 
#import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver import ChromeOptions
import keyboard
import time

class ChromeDriver:
    #driver = uc.Chrome()
    driver = webdriver.Chrome('/Users/Mac/Desktop/Python Projects/ChromeDriver/chromedriver_mac64/chromedriver')
    driver.get('http://127.0.0.1:5500/?cmd=sb-logout&from=http%3A//127.0.0.1%3A5500/main.html')
    driver.find_element(By.ID,'sbLogInCta').click()
    try:
        wait = WDW(driver, 10).until(EC.presence_of_element_located((By.ID, 'sbLogInCta')))
    except:
        pass
    time.sleep(2) 
    driver.find_element(By.ID, 'sbxJxRegEmail').send_keys('WillCatonJr@Gmail.com')
    time.sleep(1)
    driver.find_element(By.ID, 'sbxJxRegPswd').send_keys('Comm@nd5354')
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'loginSubmitButton').send_keys(Keys.RETURN)
    time.sleep(3)
    WDW(driver, 10).until(EC.presence_of_element_located((By.ID, 'http://127.0.0.1:5500/main.html?__mBfuPAgT=d98779d054b33517d61f5d7b6454497cf2293879b762cba0552e9588435541f5&redirectUrl=&rhash=887dab383246ae9c9d7886a0e0342194&isLoginPage=true&rv=ent&emailAddress=willcatonjr%40gmail.com&password=Comm%40nd5354&persist=on')))
    time.sleep(2)
    def Overlays(driver):
        chromeOptions = ChromeOptions()
        prefs = {"credentials_enable_service": False,
            "profile.password_manager_enabled": False}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path=r'/Users/Mac/Desktop/Python Projects/ChromeDriver/chromedriver_mac64/chromedriver')
    keyboard.press_and_release('esc')
    time.sleep(3)
    

    
    
