import speech_recognition as sr
#create object of Recognizer
s=sr.Recognizer()
print ("i am your script and litstening you......")
with sr.Microphone() as m:
     audio=s.listen(m)
     query=s.recognize_google(audio, language=' eng - in ')
     print(query)