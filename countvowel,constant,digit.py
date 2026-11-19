def count_characters(s):
    vowels_set = set("aeiouAEIOU")
    vowels = 0
    consonants = 0
    digits = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels_set:
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1

    return vowels, consonants, digits