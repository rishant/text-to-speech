# https://www.youtube.com/watch?v=buoSzgX9yM4&t=339s
# https://www.youtube.com/watch?v=kyZ_5cvrXJI

# https://www.youtube.com/watch?v=gXuEspYdcYk

# pip install pyttsx3

import pyttsx3

text_speech = pyttsx3.init()
# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

answer = input(mytext)
text_speech.setProperty('rate', 300)
text_speech.say(answer)
text_speech.runAndWait()