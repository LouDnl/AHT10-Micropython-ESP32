"""
This main.py is an example of how to use the AHT10 Micropython library
LouDFPV 20-12-2020
"""

import time # for the sleep function

from aht10 import AHT10 # import the module
aht = AHT10(0x38, 21, 22) # i2c address, sclPin, sdaPin


while True: # infinite loop
	aht.printInfo() # prints the Temperature and Humidity to the console

	temp = aht.temperature() # get the temperature and assign it to the temp variable
	humi = aht.humidity() # get the humidity and assign it to the humi variable
	print(u'Temperature: {0:.2f}C'.format(temp)) # print the temperature to the console formatted with 2 decimals
	print(u'Humidity: {0:.2f}%'.format(humi)) # print the humidity to the console formatted with 2 decimals
	time.sleep(10) # sleep 10
