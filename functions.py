import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 12
GREEN = 16
LAMP = 26

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(LAMP, GPIO.OUT)


def interpret_text(command):
    if command == "never mind":
        pass

    elif command == "turn on desk light":
        GPIO.output(RED, GPIO.HIGH)
        print("turning on desk light")
        GPIO.output(LAMP, GPIO.LOW)
        time.sleep(3)
        GPIO.output(RED, GPIO.LOW)

    elif command == "turn off desk light":
        GPIO.output(RED, GPIO.HIGH)
        print("turning off desk light")
        GPIO.output(LAMP, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(RED, GPIO.LOW)

    else:
        pass


def red_off():
    GPIO.output(RED, GPIO.LOW)


def green_off():
    GPIO.output(GREEN, GPIO.LOW)


def green_on():
    GPIO.output(GREEN, GPIO.HIGH)


def red_on():
    GPIO.output(RED, GPIO.HIGH)
