from spellchecker import SpellChecker
import re

# A way to detect languages

language = 'en'

spell_checker = SpellChecker(language=language)

def spell_check(text):
    words = re.findall(r'\b\w+\b', text.lower())

    misspelled = spell_checker.unknown(words)

    score = len(misspelled) / len(words) if words else 0

    message = ""

    match score:
        case s if s == 0.0:  # No misspellings, perfect score
            message = "No misspellings found."
        case s if s >= 0.0 and s < 0.02:  # No misspellings, perfect score
            message = "Some minor misspellings found, but overall good."
        case s if s >= 0.02 and s < 0.04:  # No misspellings, perfect score
            message = "Some misspellings found, please review."
        case s if s >= 0.04 and s < 0.08:  # No misspellings, perfect score
            message = "Several misspellings found, please review carefully."
        case s if s >= 0.08:  # No misspellings, perfect score
            message = "Many misspellings found, please review thoroughly."
    return score, message