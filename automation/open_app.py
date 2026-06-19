import os
import webbrowser

def open_application(command):
    
    command = command.lower()

    if "chrome" in command:
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "github" in command:
        webbrowser.open("https://github.com")

    elif "calculator" in command:
        os.system("calc")

    elif "notepad" in command:
        os.system("notepad")

    else:
        return "Application not found"

    return "Done"
