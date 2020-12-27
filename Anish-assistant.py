import wikipedia
import pyjokes
import pywhatkit
import Endtime
print("Ready to speak")
cmd = input()

if "Anish" in cmd: 
    cmd = cmd.replace("Anish",'')
    if "who is" in cmd:
        cmd = cmd.replace("who is","")
        print(cmd)
        result = wikipedia.summary(cmd,5)
        print(result)
    elif "play" in cmd:
        
        pywhatkit.playonyt(cmd)
    elif "joke" in cmd:
        print (pyjokes.get_joke(category="neutral"))
    elif "time" in cmd:
        Endtime.time()
    else:
        print("Couldn't understand your command")

 
    
