from spell_check import spell_check
from attachment_check import attachment_check

def scam_detection(email_body, attachments=None):

	# Grammar score:
	spell_score, spell_message = spell_check(email_body)
	print(f"Grammar score: {spell_score, spell_message}")

    # Attachments score:
	if attachments:
		attachment_score, attachment_message = attachment_check(attachments)
		print(f"Attachment score: {attachment_score}")
		
	# Total score:
	# total_score = (spell_score + attachment_score) / 2
	# print(f"Total score: {total_score}")

	return 

scam_detection("This is a testss hello. 33 email with no grammatical errors.")