import sys

def main():
    argument = sys.argv[1]

    every_other = ""
    capitalized = True

    asterisk_vowels = ""
    vowels = ["A", "E", "I", "O", "U"]

    opening_parentheses_count = 0
    closing_parentheses_count = 0
    balanced = True
    for character in argument:
        #strings
        if character.upper() != character.lower():
            if capitalized:
                character = character.upper()
                capitalized = not(capitalized)
            else:
                character = character.lower()
                capitalized = not(capitalized)
        every_other += character
        if character in vowels: asterisk_vowels += "*"
        else: asterisk_vowels += character

        if character == "(" and balanced:
            opening_parentheses_count += 1
        elif character == ")" and balanced:
            closing_parentheses_count += 1
            if opening_parentheses_count < closing_parentheses_count:
                balanced = False

    if opening_parentheses_count != closing_parentheses_count:
        balanced = False
    
    print(every_other)
    print(asterisk_vowels)
    print("Balanced? {}".format(balanced))

main()