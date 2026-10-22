def longestCommonPrefix(strs) -> str:
    if not strs: return ""
    s1, s2 = min(strs), max(strs)
    return "".join(s1[i] for i in range(len(s1)) if s1[i] == s2[i])