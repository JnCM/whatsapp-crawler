from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time

class WhatsappCrawler:
    def __init__(self, url="https://web.whatsapp.com/"):
        self.__driver = webdriver.Chrome()
        self.__wait = WebDriverWait(self.__driver, timeout=60)
        self.__base_url = url
        self.__driver.get(self.__base_url)
        self.__contact = ""
        self.__msg_to_wait = ""
        self.__msg_to_send = ""
    
    def connect_smartphone(self):
        self.__wait.until(lambda d : d.find_element(By.CLASS_NAME, "_akau"))
        print("== Escaneie o QR-Code para conectar... ==")
        self.__wait.until(lambda d : d.find_element(By.XPATH, '//div[@title="Chats"]'))
        time.sleep(15)
        print("== Whatsapp conectado com sucesso! ==")
    
    def set_contact(self, contact):
        if contact != self.__contact:
            self.__contact = contact
            chat = self.__driver.find_element(By.XPATH, f"//span[@title='{self.__contact}']")
            chat.click()
            print("== Contato/Grupo selecionado! ==")

    def set_msg_to_send(self, msg_to_send):
        self.__msg_to_send = msg_to_send

    def send_message(self):
        text_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        msg_box = self.__driver.find_element(By.XPATH, text_box_xpath)
        msg_box.send_keys(self.__msg_to_send + Keys.ENTER)
        time.sleep(3)
        print("== Mensagem enviada com sucesso! ==")

    def wait_for_message(self, msg_to_wait):
        self.__msg_to_wait = msg_to_wait
        has_target = False
        while not has_target:
            chat_historic = self.__driver.find_element(By.CLASS_NAME, '_ajyl')
            messages = chat_historic.find_elements(By.TAG_NAME, 'div')
            for msg in messages:
                try:
                    if msg.get_attribute("role") is not None:
                        if msg.get_attribute("role") == "row":
                            contents = msg.find_elements(By.TAG_NAME, 'span')
                            for content in contents:
                                if content.text is not None:
                                    if self.__msg_to_wait in content.text:
                                        has_target = True
                                        print("== Mensagem esperada lida com sucesso! ==")
                                        break
                            if has_target:
                                break
                except StaleElementReferenceException:
                    pass
        if has_target:
            self.send_message()
    
    def close_session(self):
        self.__driver.quit()   
