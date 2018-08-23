import speech_recognition as sr
import pyperclip
import webbrowser
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
	audio = r.listen(source)
url ='https://www.google.co.in/search?&q='+r.recognize_google(audio)
webbrowser.open_new(url)

#f= open("output.txt","w+")
#f.write(r.recognize_google(audio))
#pyperclip.copy(r.recognize_google(audio))
#harvard = sr.AudioFile('harvard.wav')
#with harvard as source:
#	audio = r.record(source)