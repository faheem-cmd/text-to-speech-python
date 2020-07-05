import pyttsx3


def text_to_speech(v):
    sample=pyttsx3.init()
    sample.say("{}".format(v))
    sample.runAndWait()


v = "hello world "

text_to_speech(v)