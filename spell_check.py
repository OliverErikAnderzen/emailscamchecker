from spellchecker import SpellChecker
import re

# A way to detect languages

language = 'en'

spell_checker = SpellChecker(language=language)

def spell_check(text):
    words = re.findall(r'\b\w+\b', text.lower())

    misspelled = spell_checker.unknown(words)

    score = len(misspelled) / len(words) if words else 0

    return score