import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Initialize browser to go to the link
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
browser.implicitly_wait(10)

game = browser.find_element_by_class_name('html')

while True:
    game.send_keys(Keys.UP)
    game.send_keys(Keys.RIGHT)
    game.send_keys(Keys.DOWN)
    game.send_keys(Keys.LEFT)


