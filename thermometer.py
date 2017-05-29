#!/usr/bin/env python

import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-000004abf982/w1_slave'

def read_sensor():
    with open(temp_sensor, 'r') as file:
        lines = file.readlines()
    return lines


def read_temp():
    data = read_sensor()
    while 'YES' not in data[0]:
        time.sleep(0.2)
        data = read_sensor()
    temperature = data[1][data[1].find('=') + 1:]
    temperature = float(temperature) / 1000.0
    return temperature


if __name__ == '__main__':
    print(read_temp())