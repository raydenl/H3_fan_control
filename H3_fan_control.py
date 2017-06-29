''' THIS SCRIPT CONTROL Orange Pi FAN FOR H3 BASED BOARD
    Create a CRON job to make it run as service, edit CRON as Super User
    to give permission for file control GPIO. 
    CRON JOB EXAMPLE: @reboot /path_to_file/H3_fan_control.py
'''
__author__ = "Vanderlei"

# Used PIN 40 (PG7) 

import subprocess
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

### Return Armbian CPU temperature
def get_temp():

    sp = subprocess
    temp_1 = ["cat","/sys/devices/virtual/thermal/thermal_zone0/temp"]
    temp_2 = ["cat","/sys/devices/virtual/thermal/thermal_zone1/temp"]

    command = sp.Popen(temp_1, stdout=sp.PIPE)
    output, err = command.communicate()
    temp_1 = int(output)

    command = sp.Popen(temp_2, stdout=sp.PIPE)
    output, err = command.communicate()

    #Armbian has 2 temp meters for CPU
    temp_final = (temp_1 + int(output)) // 2

    return temp_final

#Change fan state if temp is over 60C
def fan_state(temp):
    if temp > 40:
        #Debug line
        #print "CPU temp: " + str(temp) + "C" + " - Fan On!"

        #Change output state
        gpio.output(port.PG7, gpio.HIGH)
        #Turn on fan at least 60 seconds
        sleep(60)
    else:
        #Debug line
        #print "CPU temperature: " + str(temp) + "C" + " - Fan Off!"

        #Turn off fan
        gpio.output(port.PG7, gpio.LOW)

#Work as service, every 10 seconds
def main():
    while True:
        fan_state(get_temp())
        sleep(10)


gpio.init()
gpio.setcfg(port.PG7, gpio.OUTPUT)

main()