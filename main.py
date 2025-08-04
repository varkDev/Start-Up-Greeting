import os
import datetime
import pyttsx3
import sys
import json

def get_config_path():
    return os.path.join(os.path.expanduser("~"), ".greet_config.json") #expanduser is the function that expands from the home dir "~" e.g. C:\Users\username\.greet_config.json

def get_shortcut_path():
    return os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'GreetMe.lnk') #creating the shortcut in the startup folder, it is also giving it the name GreetMe.lnk which is a shortcut extension

def get_saved_name(config_path):
    if os.path.exists(config_path): #if the config file containing the name exists
        with open(config_path, 'r') as f:
            data = json.load(f) #load the json within the file into var data
            return data.get("username") #return the "username" key from the data
    return None #else return None

def save_name(config_path, name):
    with open(config_path, 'w') as f:
        json.dump({"username": name}, f) #basically json dump/stores the name in the config file as a json object with the key "username"

def greet_user(name):
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    message = f"{greeting}, {name}" #greeting message based on the time of the day and the user's name
    engine = pyttsx3.init() #initializing the text-to-speech engine
    engine.say(message) #using the text-to-speech engine to say the greeting message
    engine.runAndWait() #wait for the speech to finish before continuing

def add_to_startup(script_path, shortcut_path):
    try:
        import pythoncom #importing pythoncom to ensure COM support is available
        import win32com.client #importing win32com.client to create a Windows shortcut
        shell = win32com.client.Dispatch("WScript.Shell") #create a shell object to interact with the Windows shell
        shortcut = shell.CreateShortCut(shortcut_path) #create a new shortcut object
        shortcut.TargetPath = sys.executable #set the target path to the Python executable, python can't run .py files directly from the startup folder, so we use the executable
        shortcut.Arguments = f'"{script_path}" --silent' #open the script with the --silent argument to avoid showing the menu on startup - basically for a split second
        shortcut.WorkingDirectory = os.path.dirname(script_path) #set the working directory to the script's directory, so it can access any resources relative to the script
        shortcut.IconLocation = sys.executable #use the Python executable as the icon for the shortcut
        shortcut.save() #save the shortcut to the specified path
        print("✅ Setup complete. Added to startup.")
        engine = pyttsx3.init() #initialize the text-to-speech engine
        engine.say("Setup complete. I will greet you on startup.") #say the setup complete message
        engine.runAndWait() #wait for the speech to finish before continuing
    except Exception as e:
        print(f"⚠️ Failed to set up startup shortcut: {e}") #handle any exceptions that occur during the setup process

def remove_from_startup(shortcut_path, config_path):
    removed_shortcut = False #flag to track if the shortcut was removed
    removed_config = False #flag to track if the config was removed

    if os.path.exists(shortcut_path): #check if the shortcut exists
        os.remove(shortcut_path) #remove the shortcut file
        print("✅ Removed from startup.")
        removed_shortcut = True #set the flag to True
    else:
        print("⚠️ No startup shortcut found.")

    if os.path.exists(config_path): #check if the config file exists
        os.remove(config_path) #remove the config file
        print("✅ Removed saved name configuration.")
        removed_config = True #set the flag to True
    else:
        if removed_shortcut:
            print("⚠️ No saved name configuration found.")

def reset_name(config_path):
    if os.path.exists(config_path): #check if the config file exists
        os.remove(config_path) #remove the config file
        print("✅ Name reset. You’ll be asked again next time.")
    else:
        print("⚠️ No saved name found.")

def show_menu():
    config_path = get_config_path() #get the path to the config file
    shortcut_path = get_shortcut_path() #get the path to the startup shortcut
    script_path = os.path.abspath(sys.argv[0]) #get the absolute path of the current script

    while True:
        print("\nWelcome! What would you like to do?")
        print("1. Add greeting (or greet if already added)")
        print("2. Remove from startup")
        print("3. Reset name")
        print("4. Exit")

        choice = input("Choose (1-4): ").strip() #strip any leading/trailing whitespace from the input

        if choice == "1":
            if not os.path.exists(shortcut_path): #check if the shortcut does not exist
                name = get_saved_name(config_path) #try to get the saved name from the config file
                if not name: #if no name is saved, ask the user for their name
                    name = input("What name should I call you? ").strip() #strip any leading/trailing whitespace from the input
                    save_name(config_path, name) #save the name in the config file
                add_to_startup(script_path, shortcut_path) #add the script to the startup folder
                greet_user(name) #greet the user with the saved name
            else:
                name = get_saved_name(config_path) 
                if not name: #if no name is saved, ask the user for their name
                    name = input("What name should I call you? ").strip() #strip any leading/trailing whitespace from the input
                    save_name(config_path, name) #save the name in the config file
                greet_user(name) # greet the user with the saved name

        elif choice == "2":
            remove_from_startup(shortcut_path, config_path)  #remove the script from the startup folder and the saved name configuration

        elif choice == "3":
            reset_name(config_path) #reset the saved name in the config file

        elif choice == "4":
            print("Goodbye!") #exit the program
            break

        else:
            print("Invalid choice. Please select 1-4.") #prompt the user to enter a valid choice

if __name__ == "__main__":
    if "--silent" in sys.argv: #check if the script is run with the --silent argument
        config_path = get_config_path() #get the path to the config file
        name = get_saved_name(config_path) #try to get the saved name from the config file
        if not name:
            name = input("What name should I call you? ").strip() #ask the user for their name if no name is saved
            save_name(config_path, name) #save the name in the config file
        greet_user(name) #greet the user with the saved name
    else:
        show_menu() #show the menu for user interaction if the script is not run with the --silent argument
