from time import sleep
from selenium import webdriver,common
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    heroURL="http://the-internet.herokuapp.com"
    heroAuthURL="http://admin:admin@the-internet.herokuapp.com/basic_auth"
    ser = Service("C:\\Users\\DLF\\chrdriv\\chromedriver.exe")
    op = webdriver.ChromeOptions()
    s = webdriver.Chrome(service=ser, options=op)
    s.get(heroAuthURL)
    sleep(.1)
    s.get(heroURL)
    s.find_element(By.XPATH,"//a[@href='/upload']").click()
    sleep(1)
    s.find_element(By.ID,'file-upload').send_keys("C:\\Users\\DLF\\Pictures\\classic.png")
    s.find_element(By.ID,'file-submit').click()
    s.get(heroURL)
    s.find_element(By.XPATH,"//a[@href='/download_secure']").click()
    s.find_element(By.XPATH,"//a[@href='download_secure/classic.png']").click()
    s.get(heroURL)
    s.find_element(By.XPATH,"//a[@href='/shifting_content']").click()
    linkList=s.find_elements(by=By.CSS_SELECTOR,value=".example>a")
    newLinkList=[]
    for link in linkList:
        newLinkList.append(link.get_attribute("href"))
    for link in newLinkList:
        original_window = s.current_window_handle
        s.switch_to.new_window('window')
        s.get(link)
        s.switch_to.window(original_window)
    s.quit()