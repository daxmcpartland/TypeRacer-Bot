import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# if you want to join a random lobby don't enter anything
lobbyURL = input("Custom lobby URL: ")

driver = webdriver.Chrome()
if lobbyURL == "":
    driver.get("https://play.typeracer.com/")
else:
    driver.get(lobbyURL)

print("[Running]")

# click start button
if lobbyURL == "":
    while(True):
        try:
            driver.find_element(By.CLASS_NAME, 'bkgnd-green')
            break
        except:
            continue   
else:
    while(True):
        try:
            driver.find_element(By.CLASS_NAME, 'raceAgainLink')
            break
        except:
            continue   

time.sleep(.25)

if lobbyURL == "":
    pyautogui.hotkey('ctrl', 'alt', 'i')
else:
    pyautogui.hotkey('ctrl', 'alt', 'k')

time.sleep(.25)

# wait until start of race
while(True):
    try:
        driver.find_element(By.CLASS_NAME, 'trafficLight')
    except:
        break

time.sleep(.0001)
typingText = driver.find_element(By.CLASS_NAME, 'inputPanel')
text = typingText.text
      
# weird equation used to keep the speed below sus level
intervalDiff = .0067 + (len(text) / 30000) 

#interval means how fast typing between letters.
pyautogui.typewrite(text, interval = intervalDiff)
time.sleep(10)
