def capitalize_words(sentence):
    words = sentence.split()
    return " ".join(word.capitalize() for word in words)