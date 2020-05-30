import speech_recognition as sr
import RPi.GPIO as GPIO
import time

r = sr.Recognizer()
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

    elif command == "turn off desk light":
        GPIO.output(RED, GPIO.HIGH)
        print("turning off desk light")
        GPIO.output(LAMP, GPIO.HIGH)
        time.sleep(3)

    else:
        pass


def get_text(s):
    print('say something')
    audio = r.listen(s, timeout = 3)

    try:
        text = r.recognize_google(audio, key=None, language='en-US')

    except sr.RequestError:
        text = r.recognize_sphinx(audio, language="en-US")

    except sr.UnknownValueError:
        text = "unknown error occurred"

    return text


with sr.Microphone(device_index=2, sample_rate = 16000, chunk_size = 1024) as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print(r.energy_threshold)
    r.dynamic_energy_threshold = False

    while True:
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(GREEN, GPIO.LOW)

        t = get_text(source).lower()
        print(t)
        if t == "hey assistant":
            GPIO.output(GREEN, GPIO.HIGH)
            user_text = get_text(source).lower()
            interpret_text(user_text)
