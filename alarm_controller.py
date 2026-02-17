#! /usr/bin/env python
# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use

from adafruit_extended_bus import ExtendedI2C as I2C
# Import the ExtendedI2C class from adafruit_extended_bus
import board  # Import the board module
import busio  # Import the busio module
import adafruit_drv2605  # Import the adafruit_drv2605 module
import drivers  # Import the drivers module
import RPi.GPIO as GPIO  # Import the RPi.GPIO module
import time  # Import the time module
from time import sleep  # Import the sleep function from the time module
from datetime import datetime  # Import the datetime class from the datetime module

# Load the driver and set it to "display"
# If you display use something from the driver library use the "display." prefix
display = drivers.Lcd()  # Initialize the LCD display

# Get user input for alarm time and alarm strength
alarm = input("Enter Alarm Time:")
strength = input("How strong do you want the alarm? (Low, Medium, High)")
# strength = input("Enter Alarm Strength:")
display.lcd_display_string("Alarm: "+alarm, 1)  # Display the entered alarm time on the LCD

# Set up I2C communication and initialize the DRV2605 haptic driver based on the selected alarm strength
i2c = I2C(3)
drv = adafruit_drv2605.DRV2605(i2c)
if(strength == "Low"):
    drv.sequence[0] = adafruit_drv2605.Effect(119)
elif(strength == "Medium"):
    drv.sequence[0] = adafruit_drv2605.Effect(1)
else:
    drv.sequence[0] = adafruit_drv2605.Effect(47)

GPIO.setwarnings(False)  # Disable GPIO warnings

try:
    while True:
        timme = str(datetime.now().time())
        if(timme[0:5] == alarm):
            drv.play()  # Trigger the haptic feedback when the alarm time is reached
        # Write just the time to the display
        display.lcd_display_string(str(datetime.now().time()), 2)
        # Uncomment the following line to loop with a 1-second delay
        sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program
    print("Cleaning up!")
    display.lcd_clear()  # Clear the LCD display upon program termination
