# The Robotspeaker


import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")

if __name__=="__main__":
    while True:
        print("Hii I am a robospeaker created by Ayush")
        x=input("Enter what you want  to speak:\n")
        if x=="q":
            text="Bye Bye freind the process has been finished"
        
            speak.Speak(text)
            break
        speak.Speak(x)
        
        


                      
