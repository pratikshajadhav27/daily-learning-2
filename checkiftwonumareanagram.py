def anagram(n1: int, n2: int) -> bool:
    # Convert numbers to strings and compare sorted characters
    return sorted(str(n1)) == sorted(str(n2))