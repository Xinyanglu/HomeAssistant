import speech_recognition as sr
import pyttsx3
import RPi.GPIO as GPIO

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

    elif command == "turn off desk light":
        GPIO.output(RED, GPIO.HIGH)
        print("turning off desk light")

    else:
        pass


def get_text(s):
    print('test')
    audio = r.listen(s)

    try:
        text = r.recognize_google(audio, key=None, language='en-US')

    except sr.RequestError:
        text = r.recognize_sphinx(audio, language="en-US")

    except sr.UnknownValueError:
        text = "unknown error occurred"

    return text


with sr.Microphone(device_index=1) as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print(r.energy_threshold)
    r.dynamic_energy_threshold = False

    while True:
        t = get_text(source).lower()
        print(t)
        if t == "hey assistant":
            GPIO.output(GREEN, GPIO.HIGH)
            user_text = get_text(source).lower()
            interpret_text(user_text)