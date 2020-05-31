import speech_recognition as sr
import functions

r = sr.Recognizer()


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


with sr.Microphone(device_index=2, sample_rate = 16000, chunk_size=1024) as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print(r.energy_threshold)
    r.dynamic_energy_threshold = False

    while True:
        t = get_text(source).lower()
        print(t)
        if t == "hey assistant":
            user_text = get_text(source).lower()
            functions.interpret_text(user_text)
