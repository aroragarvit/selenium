import selenium
from selenium import webdriver
import time
import requests

bot = webdriver.Chrome(executable_path="chromedriver.exe")
bot.get("https://www.timeanddate.com/weather/india/jaipur/hourly")
time.sleep(4)
while True:
    temp=bot.find_element_by_css_selector('body > div.main-content-div > main > article > div.weather-graph > div.weatherTooltip > div.inner__block > div.left__block > div.tempblock > div.temp')
    current_temperature = temp.text
    print(temp.text)
    time.sleep(1)

    humidity=bot.find_element_by_css_selector('body > div.main-content-div > main > article > div.weather-graph > div.weatherTooltip > div.inner__block > div.mid__block > div:nth-child(2)')
    current_humidity=humidity.text
    current_humidity_no=current_humidity[9::]
    print(current_humidity)
    time.sleep(1)

    precipate=bot.find_element_by_css_selector('body > div.main-content-div > main > article > div.weather-graph > div.weatherTooltip > div.inner__block > div.mid__block > div:nth-child(4)')
    current_precipate=precipate.text
    current_precipate_no=current_precipate[21::]
    print(current_precipate)

    time.sleep(3)

    thingspeak=requests.get('https://api.thingspeak.com/update?api_key=1IQXSTEZQJXK1RG7&field1={}&field2={}&field3={}'.format(current_temperature,current_humidity_no,current_precipate_no))


  
    continue
    
    
