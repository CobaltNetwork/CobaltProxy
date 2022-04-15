
import os
os.system("pip install selenium==3.141.0")
from webbot import Browser
import time

driver = Browser()

time.sleep(5)
driver.go_to('google.com')



driver.new_tab(url='https://madgeckos.ml')

input("Service is running")
