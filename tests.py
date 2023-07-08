from models import Synthesizer
from models import Recognizer
from models import G1NewsExtractor

import time
import unidecode

vs = Synthesizer.VoiceSynthesizer(volume=1, rate=180)
# vs.say("Olá, diga algo...")

# recon = Recognizer.VoiceRecognizer()
# frase = recon.listen()
# vs.say(f"Voce disse: {frase}")
# print(f"Voce disse: {frase}")

ns = G1NewsExtractor.NewsExtractor()
news = ns.fetchNews()
vs.say("Olá, essas são as principais notícias do dia: ")
for currentNews in news:
    print(unidecode.unidecode(
        currentNews['title'] + ', ' + currentNews['resume']))
    vs.say(currentNews['title'] + ', ' + currentNews['resume'])
    time.sleep(2)
