# H3_fan_control
Fan Control for Orange Pi H3 boards writen in Python

   To start you will need the python headers and library installed, if you haven't or aren't sure just type:
   
    sudo apt-get install python-dev
    
   Install H3 GPIO Python git Repository:
    
    git clone https://github.com/duxingkei33/orangepi_PC_gpio_pyH3
    cd orangepi_PC_gpio_pyH3
    sudo python setup.py install
    
   Create a CRON job to make it run as service, edit CRON as Super User
   to give permission for file control GPIO.
   CRON JOB EXAMPLE: 
   
    sudo crontab -e
    
   Add line to CRON file or you've created: 
   
    @reboot /path_to_file/H3_fan_control.py 
   "path_to_file" is where you saved H3_fan_control.py
   
   Now the script will run like service and check for temperature above 60 Celsius degree
   for every 10 seconds
   
   The PIN for control fan is 40 named PG7
