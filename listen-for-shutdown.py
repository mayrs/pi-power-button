#!/usr/bin/env python

from gpiozero import Button
from signal import pause
import subprocess

def longpress():
    subprocess.call(['shutdown', '-h', 'now'], shell=False)

button = Button(3, hold_time=3)
button.when_held = longpress

pause()
