import onionGpio
import time

# specify sleep duration to be used in the program
sleepTime = 0.15

# create and populate a list to hold the GPIO pin numbers that control the LEDs
gpioPins = [0, 1, 2, 3, 18, 19]
# create an empty list that will hold the GPIO objects to control the LEDs
gpioObjects = []

# print which GPIOs are being used
print 'Using GPIOs:'
for gpioElement in gpioPins:
    print gpioElement

# populate the gpioObjects list
for gpioElement in gpioPins:
    # instantiate a GPIO object for this gpio pin
    ledObj = onionGpio.OnionGpio(gpioElement)        
    # set to output direction with zero being the default value
    ledObj.setOutputDirection(0)
    # add the GPIO object to our list
    gpioObjects.append(ledObj)

# create a variable to hold the value of the LED
ledValue     = 1

# run the loop 4 times
n = 0
print n
while n < 4:
    # program all of the GPIOs to the ledValue
    for gpio in gpioObjects:
        gpio.setValue(ledValue)
        # pause after each LED is turned on or off
        time.sleep(sleepTime)

    # flip the value variable
    if ledValue == 1:
        ledValue = 0
    else:
        ledValue = 1

    n += 1
    print n
