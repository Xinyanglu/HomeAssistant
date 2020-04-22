import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def interpret_text(t):
    if t == "never mind":
        pass


while True:
    try:
        with sr.Microphone() as source:
            print('test')
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

            text = r.recognize_google(audio, key=None, language='en-US')

            interpret_text(text)

            print(text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
