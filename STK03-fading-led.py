import time
import os

# specify sleep duration to be used in the program
sleepTime = 0.1


# define other program parameters
brightnessIncrement  = 2
dutyCycle = 0

# create a PWM signal using the fast-gpio system utility
def pwmLed(pin, frequency, dutyCyclePercentage):
    # create a string to hold our command line code,assign the function arguments to fast-gpio command arguments
    command = "fast-gpio pwm %d %d %d" % (pin, frequency, dutyCyclePercentage)
    # execute the command using the OS
    os.system(command)

# infinite loop - runs main program code continuously
while 1:
    # Increment the duty cycle by the brightnessIncrement
    dutyCycle=dutyCycle+brightnessIncrement

    # Assign GPIO 0 to the pwm duty cycle value
    pwmLed(0, 50, dutyCycle)

    # flip the value variable
    if (dutyCycle <= 0) or (dutyCycle >= 100):
        # Reverse direction at 0, and 100
        brightnessIncrement = -brightnessIncrement

    # make the program pause
    time.sleep(sleepTime)