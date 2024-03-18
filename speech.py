import speech_recognition as sr

mic = sr.Microphone()
rec = sr.Recognizer()

def speech_rec():
    with mic as audio_file:
        rec.adjust_for_ambient_noise(audio_file)
        audio = rec.listen(audio_file)
        res = rec.recognize_google(audio, language="ru-RU")
        
    return res
