import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    print(voice.id, voice.name)
    engine.say('the quick brown dog jumped over the lazy dog')
engine.runAndWait()