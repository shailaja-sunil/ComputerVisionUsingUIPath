import speech_recognition as sr


r=sr.Recognizer()

with sr.Microphone() as source:
    Print('Say somthing')
    audio = r.listen((source))
    voice_data = ''
    try:
         voice_data = r.recognize_google(audio)
         print(voice_data)
    except sr.UnKnownValueError:
        print('Sorry, I did not get that')
    except sr.RequestError:
        print('Sorry, my speech sevice is down')