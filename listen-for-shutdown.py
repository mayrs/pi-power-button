#!/usr/bin/env python


from gpiozero import Button
import subprocess

perform_halt = 0

def longpress():
    global perform_halt
    perform_halt = 1

button = Button(3, hold_time=2)
button.when_held = longpress

button.wait_for_press()
button.wait_for_release()

if (perform_halt):
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
else:
    subprocess.call(['shutdown', '-r', 'now'], shell=False)
