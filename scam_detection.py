import language_tool_python as ltp

language = 'en-US'

tool = ltp.LanguageTool(language)

def scam_detection(email_body, attachments=None):
	
	total_score = 0

	# Grammar score:
	grammatical_errors = tool.check(email_body)
	total_words = len(email_body.split())
	if total_words == 0: return "safe"
	grammar_score = 1 - (len(grammatical_errors) / total_words)
	
    # Attachments score:
	# check for suspicious attachments
	
	print(f"Grammar score: {grammar_score}")
	
	return total_score

scam_detection("This is a test email with no grammatical errors.")