from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from os import path, environ
from time import sleep
from dotenv import load_dotenv

try:
    # System path helper
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = path.dirname(__file__)
        return path.join(base_path, relative_path)

    # Loading values from .env
    load_dotenv()
    refreshTimer = int(environ.get('REFRESH_TIMER', '3'))
    email = environ.get('EMAIL', '')
    password = environ.get('PASSWORD', '')

    # Initial setup
    currentSong = ''
    driver = webdriver.Firefox(executable_path=resource_path('.\driver\geckodriver2.exe'))

    # Open login page
    driver.get("https://www.epidemicsound.com/login/")
    if email != '' and password != '':
        driver.find_element_by_css_selector("#email-address1").send_keys(email)
        driver.find_element_by_css_selector("#password2").send_keys(password)
        driver.find_element_by_css_selector(".src-mainapp-auth-___LoginForm__loginButton___3sHJN").click()

    # Main loop for fetching song name
    while True:
        try:
            songName = driver.find_element_by_css_selector('.src-mainapp-player-components-___TrackInfo__title___1NuSH')
            artistName = driver.find_element_by_css_selector('.src-mainapp-components-___CreativesLabel__container___3Wf4k > a:nth-child(1)')
            if songName.text != None and artistName.text != None:
                musicData = f'{artistName.text} - {songName.text}'
                if currentSong != musicData:
                    currentSong = musicData
                    print(f'Playing: {musicData}')
                    with open('music_info.txt', 'w') as f:
                        f.write(musicData)
        except:
            pass
        sleep(refreshTimer)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sleep(15)
