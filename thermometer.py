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


if __name__ == '__main__':
    print(read_sensor())