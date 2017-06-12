import onionGpio
import time

# specify sleep duration to be used in the program
sleepTime = 2

# set which GPIOs will be used
switchPin     = 0      # use GPIO0
ledPin        = 1      # use GPIO1


# instantiate GPIO objects
switch        = onionGpio.OnionGpio(switchPin)
led           = onionGpio.OnionGpio(ledPin)

# set the GPIO directions
switch.setInputDirection()               # switch pin is an input
led.setOutputDirection(0)                # led pin is an output

# infinite loop - runs main program code continuously
#   periodically check the switch and turn the LED on or off
while 1:
    # read the switch value
    switchValue = switch.getValue()
    # turn the LED on/off depending on the switch
    led.setValue(switchValue)

    # make the program pause
    time.sleep(sleepTime)