import os
import requests
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()

def send_simple_message():
  	return requests.post(
  		f"https://api.eu.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",
  		auth=("api", os.getenv('MAILGUN_API_KEY')),
  		data={"from": f"Mailgun Sandbox <{os.getenv('SENDER_EMAIL')}>",
			"to": f"Oliver <{os.getenv('PERSONAL_EMAIL')}>",
  			"subject": "Hello Oliver",
  			"text": "Congratulations Oliver, you just sent an email with Mailgun! You are truly awesome!"})

send_simple_message()
print("Email sent successfully!")