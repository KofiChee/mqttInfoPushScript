# mqttInfoPushScript
This project is designed to meet the requirements laid out for the
Distributed Systems module and Open Source Software
in the Enterprise module in DT080B


This script requires python3 and the psutil and paho-mqtt modules


      apt-get install python3
      apt-get install python3-pip
      python3 -m pip install psutil
      python3 -m pip install paho-mqtt



## How to run this script every 10 minutes

On Linux, this requires the use of crontab

      crontab -e

Inside the editor, append the following

      10 * * * * /usr/bin/python3 /home/sean/mqtt.py

This will run the script every 10 minutes, assuming python3 is at
/usr/bin/python3 and the script is located in /home/sean/mqtt.py
