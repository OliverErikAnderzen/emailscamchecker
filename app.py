import os
import requests
# from dotenv import load_dotenv
from flask import Flask, request, abort

app = Flask(__name__)

# load_dotenv()

def send_simple_message(to, subject, text):
  	return requests.post(
  		f"https://api.eu.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",
  		auth=("api", os.getenv('MAILGUN_API_KEY')),
  		data={"from": f"Mailgun Sandbox <{os.getenv('SENDER_EMAIL')}>",
			"to": to,
  			"subject": subject,
  			"text": text})

@app.route("/inbound-email", methods=["POST"])
def inbound_email():
	sender = request.form.get("sender")
	subject = request.form.get("subject")
	body = request.form.get("body-plain") or request.form.get("body-html") or ""

	if not sender:
		abort(400, "Sender is required")

	# Here we add scam detection logic

	scam_status = "safe"  # Placeholder for scam detection logic
	message = ""

	if scam_status == "safe":
		message = "Your email is safe and has been processed."
	else:
		message = "Your email has been flagged as potential spam."

	send_simple_message(
		sender, 
		subject,
		body + "\n\n" + message
		)
	
	return "Email processed successfully", 200