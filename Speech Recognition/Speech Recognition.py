import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listener = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def hear():
    cmd = ""    # Initializes cmd so it always exists
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            voice = listener.listen(mic)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'Prachi' in cmd:
                cmd = cmd.replace('Prachi', '')
                print(f"Command received: {cmd}")
    except Exception as e:
        print("Error:", e)
        cmd = ""
    return cmd

def run():
    cmd = hear()
    print(f"Processing command: {cmd}")
    if 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak(f'Playing {song}')
        pk.playonyt(song)
    elif 'time' in cmd:
        from datetime import datetime
        time = datetime.now().strftime('%I:%M %p')
        speak(f'The current time is {time}')
    elif 'who is' in cmd:
        person = cmd.replace('who is', '')
        info = pk.info(person, lines=1)
        speak(info)
    else:
        speak("Please say the command again.")
        
if __name__ == "__main__":
    run()