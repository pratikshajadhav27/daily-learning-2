def count_special_chars(s):
    count = 0
    for ch in s:
        if not ch.isalnum() and not ch.isspace():
            count += 1
    return count