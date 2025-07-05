from spell_check import spell_check
from attachment_check import attachment_check
import re

language = 'en-US'

def scam_detection(email_body, attachments=None):
	
	total_score = 0

	# Grammar score:
	
	grammar_score = spell_check(email_body)
	
    # Attachments score:

	attachment_score = attachment_check(attachments)
	
	print(f"Grammar score: {grammar_score}")
	print(f"Attachment score: {attachment_score}")
	
	total_score = (grammar_score + attachment_score) / 2

	print(f"Total score: {total_score}")

	return total_score

scam_detection("This is a test email with no grammatical errors.")