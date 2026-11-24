def is_duck_number(num_str):
    if not num_str or num_str[0] == "0":
        return False
    return "0" in num_str[1:]