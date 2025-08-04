# 🎉 GreetMe: Your Personal Startup Greeter 🎉

Ever seen those movies where the computer knows your name and greets you as soon as you sit down?  
Well, now you can have a little taste of that tech magic on your own **Windows PC!** 💻✨

---

## ❓ What is this?

**GreetMe** is a simple Python script that uses **text-to-speech** to greet you by name every time you start your computer.  
It remembers your name, adjusts the greeting based on the time of day, and even sets itself up to run automatically at startup — all with just a few clicks. 🚀

---

## 🤔 Why this project?

Inspired by those cool sci-fi moments where the computer is almost alive, this project is a great way to learn how to:

- 📂 Work with **JSON** to save and load your settings  
- 🔊 Use Python's `pyttsx3` for offline **text-to-speech**  
- ⚙️ Automate tasks on Windows, like adding shortcuts to the **Startup folder**  
- 🖥️ Handle user input and program flow with menus and command-line arguments  

The code is **heavily commented**, making it easy to follow along and understand how each part works. 📝

---

## ✨ Features

- 🌅 Personalized greetings based on the time of day (morning, afternoon, evening)  
- 💾 Saves your name so you don’t have to enter it every time  
- 🔄 Adds/removes itself from Windows startup for automatic greetings  
- ♻️ Option to reset your saved name whenever you want  
- 🤫 Runs silently on startup so you’re greeted immediately without prompts  

---

## 🚀 How to use

1. Run the script normally to see the menu and set up your greeting.  
2. Choose to add the greeting to startup — your computer will greet you next time you log in!  
3. Want to reset or remove the greeting? Use the menu options anytime.  
4. Behind the scenes, the script stores your name in a config file in your home folder.  

---

## 🛠️ Requirements

| Package     | Install Command            | Purpose                            |
| ----------- | -------------------------- | ---------------------------------|
| Python 3.x  | —                          | Runs the script                   |
| `pyttsx3`   | `pip install pyttsx3`       | Offline text-to-speech engine     |
| `pywin32`   | `pip install pywin32`       | Create Windows startup shortcut   |
| Windows OS  | —                          | For startup folder & speech APIs  |

---

## 📚 Want to learn more?

Check out the **code comments** — every function and step is explained so you can learn how to build your own cool automations and personal assistants! 🤓

---

**Bring a little movie magic to your PC. Happy coding!** ✨🚀
