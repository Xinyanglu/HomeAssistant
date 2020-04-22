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

    elif t == "turn on desk light":
        # code to turn on desk light
        pass


def get_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_google(audio, key=None, language='en-US')

        except sr.RequestError as e:
            text = "Could not request results; {0}".format(e)

        except sr.UnknownValueError:
            text = "unknown error occurred"

        return text


while True:
    if get_text() == "hey assistant":
        user_text = get_text()
        interpret_text(user_text)


