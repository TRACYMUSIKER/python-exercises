text = "hello world"



def leet_speak_translator(text):
    letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
    numbers = [ 4,   3,   6,   1,   0,   5,   7]

    translation = ""
    uppercased_text = text.upper() #TRANSLATE ALL TO UPPERCASE
    for letter in uppercased_text: #iterates over all UPERCASE TEXT
        counter = 0 #starts counter, index @ 0
        # letter_to_add_to_translation = "" #empty string of letters to add
        for letter_to_convert in letters_to_convert:
            if letter == letter_to_convert: #looks over all letters in letters to convert
      # translation = translation + str(numbers[counter])
                letter_to_add_to_translation = str(numbers[counter])
                break 
            else:
      # translation = translation + letter
                letter_to_add_to_translation = letter
            counter = counter + 1
            translation = translation + letter_to_add_to_translation
    return translation

print leet_speak_translator(text)
