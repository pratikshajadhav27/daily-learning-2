def replacePi(s: str) -> str:
    res = []
    i = 0
    n = len(s)

    while i < n:
        # Check if current character and next character form "pi"
        if i + 1 < n and s[i] == "p" and s[i + 1] == "i":
            res.append("3.14")
            i += 2  # Skip both 'p' and 'i'
        else:
            res.append(s[i])
            i += 1  # Move to next character

    return "".join(res)