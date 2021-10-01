import speech_recognition as speech

def takeCommand():  #method to take audio
    r = speech.Recognizer()  #recognizer class of speech recognition
    with speech.Microphone() as source:   #taking input through microphone
        r.adjust_for_ambient_noise(source)   #adjusting noise
        print("Listening.....")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)  #google api to recognise audio
        print(f"User said : {query}\n")
        with open('textFile.txt','a+') as t:  #opening file and appending to it
            if 'thank you' not in query:
                t.write("\n" + query)     #writing in file

    except Exception as e:
        print("Sorry I cannot hear this properly, Say that again please....")
        return "None"
    return query

if __name__ == '__main__':   #main method
    while(True):
        query = takeCommand().lower()
        if 'thank you' in query:
            exit()
