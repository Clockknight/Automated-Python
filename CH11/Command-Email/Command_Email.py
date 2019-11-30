import os
import logging
import selenium
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG, format = '%(levelname)s - %(message)s')
#logging.disable(Debug)

target = input('Please input target email:\n')
logging.debug(target)
message = input('Please input intended message:\n')
logging.debug(message)
