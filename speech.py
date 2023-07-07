#pip install pyttsx3
#pip install pypiwin32

import pyttsx3

speech = pyttsx3.init('sapi5')
speech.setProperty('rate', 180)
speech.setProperty('volume', 1)
speech.setProperty('voice', b'brazil')
speech.say("Seja bem-vindo ao Leitor de Notícias, qual tipo de notícia deseja pesquisar?")
speech.runAndWait()