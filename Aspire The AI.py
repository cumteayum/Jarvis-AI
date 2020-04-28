import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
	engine.say(audio)
	print("Speaking....")
	engine.runAndWait()

def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
	
		speak("Good Morning sir")

	elif hour>=12 and hour<18:
		speak("Good Afternoon sir")

	else:
		speak("Good Evening sir")

	speak("I am jarvis, here to help you,  tell me what to do")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)    
        print("I haven't got it, say that again please")
       
       
        return "None"
    return query

if __name__ == "__main__":
	wishme()
	while True:
		query = takeCommand().lower()

		#logic for AI

		if "wikipedia" in query:
			speak("searching wikipedia......")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			print(results)
			speak("According to wikipedia")
			speak(results)

	
		elif "youtube" in query:
			speak("opening youtube.....")
			wb.open("youtube.com")


		elif "open github" in query:
			speak("opening github.....")
			wb.open("github.com")

		elif "open google" in query:
			wb.open("google.com")
			speak("opening Google")

			
		elif "play random video" in query:
			vid_dir = "E:\\Videos"
			video = os.listdir(vid_dir)
			random_file = random.choice(video)
			os.startfile(os.path.join(vid_dir, random_file))

		elif ".com" in query:
			wb.open(".com"+query)
			speak(f"opening {query}")

		elif "what is the time now" in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"the time now is{strTime}")

		elif "open stackoverflow" in query:
			wb.open("stackoverflow.com")

		elif "who are you" in query:
			speak("I am EESHAAN's personal assistant")

		elif "what is your name" in query:
			speak("I am Jaarvis sir")

		elif "play video" in query:
			speak("playing you favourite video, sir")
			os.startfile("E:\\Don Diablo - We Are Love.mp4")

		elif "open amazon" in query:
			wb.open("www.amazon.in")

		elif "open twitter" in query:
			wb.open("www.twitter.com")

		elif "speak alphabets" in query:
			speak("Speaking alphabets")
			for alpha in range(65, 91):
				speak(chr(alpha))