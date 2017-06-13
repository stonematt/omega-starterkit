# import modules and classes
import time
import sys
from datetime import datetime
from temperatureSensor import TemperatureSensor
import oneWire

# setup onewire and polling interval
oneWireGpio = 19 # set the sensor GPIO
#pollingInterval = 1 # seconds

# use command line argument to set the polling interval
print len(sys.argv)
if len(sys.argv) == 1:
    pollingInterval = 300 #if no command line argument, use 300s
    print "Polling at " + str(pollingInterval) + "s" 
else:
    pollingInterval = float(sys.argv[1])
    print "Polling at " + str(pollingInterval) + "s" 

def __main__():
    # check if 1-Wire is setup in the kernel
    if not oneWire.setupOneWire(str(oneWireGpio)):
        print "Kernel module could not be inserted. Please reboot and try again."
        return -1

    # get the address of the temperature sensor
    #   it should be the only device connected in this experiment
    sensorAddress = oneWire.scanOneAddress()

    # instantiate the temperature sensor object
    sensor = TemperatureSensor("oneWire", { "address": sensorAddress, "gpio": oneWireGpio })
    if not sensor.ready:
        print "Sensor was not set up correctly. Please make sure that your sensor is firmly connected to the GPIO specified above and try again."
        return -1

    # infinite loop - runs main program code continuously
    while 1:
        # check and print the temperature
        value = sensor.readValue()
        # print "T = " + str(value) + " C" # replaced for output with timestamp
        print str(datetime.now()) + " , " + str(value) + " C"
        time.sleep(pollingInterval)

if __name__ == '__main__':
    __main__()
