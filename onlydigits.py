def is_all_digits(s):
    if not s:
        return False
    for ch in s:
        if not ch.isdigit():
            return False
    return True