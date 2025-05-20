from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_URL = "https://x.com/i/flow/login"
SPEED_TEST_URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome()

        self.upload_speed = 0
        self.download_speed = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)

        self.upload_speed = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.download_speed = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        self.driver.quit()

    def tweet_at_provider(self, twitter_acc, twitter_pass):
        self.driver.get(TWITTER_URL)
        time.sleep(3)

        username_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        username_field.send_keys(twitter_acc)

        next_button = self.driver.find_element(By.XPATH, '//span[text()="Avançar"]/ancestor::button')
        next_button.click()
        time.sleep(5)

        password_field = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        password_field.send_keys(twitter_pass)
        time.sleep(2)

        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="LoginForm_Login_Button"]')
        login_button.click()
        time.sleep(5)

        tweet_text = f"Ô, @vivobr! {self.download_speed}Mbps de download e {self.upload_speed}Mbps de upload — isso é sério?"
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="O que está acontecendo?"]')
        tweet_input.send_keys(tweet_text)
        time.sleep(2)

        tweet_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        tweet_button.click()

        self.driver.quit()


