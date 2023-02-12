
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')

#Sentence Tokenization - Splitting sentences in the paragraph

text = "Hello Vinay, How are you. what are you doing right now"
print(sent_tokenize(text))

#Word Tokenizing
from nltk.tokenize import word_tokenize
text = "Hello Vinay. How are you, weather is great"
print(word_tokenize(text))


import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak....")
    audio = r.listen(source)
try:
    print("text:" + r.recognize_google(audio))
except Exception:
    print("Its not clear...")

#pip install pipwin
#pipwin install pyaudio

from newspaper import Article
import nltk
from gtts import gTTS
import os


test = " hi how are you, what are you doing right now, how was the weather out side"
nltk.download('punkt')
language = 'en'

myobj = gTTS(text=test, lang=language, slow=False)
myobj.save("read_article1.mp3")
os.system("start read_article1.mp3")


article = Article('https://www.bbc.com/news/science_and_environment')
article.download()
article.parse()
#nltk.download('punkt')
article.nlp()
mytext = article.text
language = 'en'
#language = 'hi'
myobj = gTTS(text=mytext, lang=language, slow=False)
#myjob = gTTS(text=test, lang=language, slow=False)
myobj.save("read_article12.mp3")
os.system("start read_article12.mp3")




   
