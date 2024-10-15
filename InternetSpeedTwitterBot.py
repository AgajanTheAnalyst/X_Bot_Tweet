from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speedtest

class InternetSpeedTwitterBot:
    def __init__(self, driver, up, down):
        self.driver = driver
        self.up = 0  # Actual measured upload speed
        self.down = 0  # Actual measured download speed
        self.upload = up  # Promised upload speed
        self.download = down  # Promised download speed

    def get_internet_speed(self):
        try:
            st = speedtest.Speedtest()
            download_speed = st.download() / 1_000_000
            upload_speed = st.upload() / 1_000_000
            self.up = upload_speed
            self.down = download_speed
        except speedtest.ConfigRetrievalError as e:
            print(f"Failed to retrieve Speedtest Configuration {e}")
        except Exception as e:
            print(f"error fetching speed {e}")

    def tweet_at_provider(self, username, password, twitter_link, message):
        # Check if internet speed is below the promised values
        if float(self.down) < float(self.download) or float(self.up) < float(self.upload):
            try:
                self.driver.get(twitter_link)

                login = WebDriverWait(self.driver, timeout=10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, 'Sign in'))
                )
                login.click()

                # Enter username and password
                username_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "text"))
                )
                username_field.send_keys(username, Keys.ENTER)

                password_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys(password, Keys.ENTER)

                # Wait for Twitter to load and then send the message
                tweet_box = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,  "div[aria-label='Tweet text']"))
                )
                tweet_box.click()
                tweet_box.send_keys(message)

                # Click the Tweet button
                tweet_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetButtonInline']"))
                )
                tweet_button.click()
            except Exception as e:
                print(f"An error occurred:{e}")

        else:
            print("Internet speed is as promised. No need to tweet.")
