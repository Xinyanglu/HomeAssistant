import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

RED = 12
GREEN = 16

def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def interpret_text(command):
    if command == "never mind":
        pass

    elif command == "turn on desk light":
        # code to turn on desk light
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
    r.adjust_for_ambient_noise(source, duration=1)
    print(r.energy_threshold)
    r.dynamic_energy_threshold = False

    while True:
        t = get_text(source).lower()
        if t == "hey assistant":

            user_text = get_text(source).lower()
            interpret_text(user_text)