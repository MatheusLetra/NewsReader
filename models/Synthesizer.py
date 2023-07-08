import pyttsx3

class VoiceSynthesizer:
    def __init__(self, rate=180, volume=1, voice=b'brazil'):
        self.speech = pyttsx3.init('sapi5')
        self.speech.setProperty('rate', rate)     # integer value
        self.speech.setProperty('volume', volume)  # float value 0 ~ 1
        self.speech.setProperty('voice', voice)

    def say(self, phrase="Olá, seja bem-vindo ao NewsReader, o seu leitor pessoal de notícias!"):
        self.speech.say(phrase)
        self.speech.runAndWait()
