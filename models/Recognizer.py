import speech_recognition as sr


class VoiceRecognizer:
    def __init__(self, language='pt'):
        self.recognizer = sr.Recognizer()
        self.language = language

    def listen(self):
        with sr.Microphone() as source:
            print("Diga algo...")
            audio = self.recognizer.listen(source)
        return self.recognizer.recognize_google(audio, language=self.language)
