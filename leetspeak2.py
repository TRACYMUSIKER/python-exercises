# -*- coding: utf-8 -*-
def leetspeaktranslator(text):
    leetspeaktranslated = ""
    leetdictionary = {
        'A': '4',
		'E': '3',
		'G': '6',
		'I': '1',
		'O': '0',
		'S': '5',
		'T': '7'
    }
    for letter in text:
        if letter.upper in leetdictionary:
            letter = leetdictionary[letter.upper] 
        leetspeaktranslated += letter
    return letspeaktranslated

nonleetsentence = "Please work. This sucks."
print leetspeaktranslator(nonleetsentence)
# print translated_from_non_leet_to_l33t
