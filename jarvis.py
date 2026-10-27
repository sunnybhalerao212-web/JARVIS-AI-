
import datetime

name = "Vishwajeet"

def jarvis():
    hour = datetime.datetime.now().hour

    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print("================================")
    print("     JARVIS AI SYSTEM ONLINE")
    print("================================")
    print(f"{greeting}, {name} Sir!")
    print("Hello! I am your Jarvis AI.")
    print("Your AI journey starts today!")

jarvis()
