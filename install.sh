#!/bin/bash

chmod +x *.sh *.py
sudo apt-get update
sudo apt-get install git-core
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
sudo apt-get install python-dev python-pip
sudo pip install wiringpi2
#if pip-3.2 can't be found, please use pip3
#sudo pip3 install python-uinput pyudev

sudo cp encoder2.py /usr/bin/
sudo cp encoder2.sh /etc/init.d/

sudo chmod +x /usr/bin/encoder2.py
sudo chmod +x /etc/init.d/encoder2.sh

sudo update-rc.d encoder.sh defaults

