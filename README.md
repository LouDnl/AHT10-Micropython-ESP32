# AHT10-Micropython-ESP32
AHT10 Micropython library for the ESP32
Based on https://github.com/gejanssen/aht10-python by @gejanssen and information found on the internet
 
## Example usage
Put the aht10.py and main.py in the folder of your project.
Upload and run.

## Using in your own code
AHT10 default i2c address is 0x38\n

```
from aht10 import AHT10\n
aht = AHT10(0x38, 21, 22) # i2c address, sclPin, sdaPin

aht.printInfo() # print temperature and humidity to the console
```

## Available methods
```
aht.printInfo() # print temperature and humidity to the console
aht.temperature() # returns temperature as float
aht.humidity() # returns humidity as float
```

## Questions?
Don't hesitate to drop me a question