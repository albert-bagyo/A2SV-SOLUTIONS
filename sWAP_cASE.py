def swap_case(s):
    result = ""
    for l in s:
        result += l.lower() if l.isupper() else l.upper()
    return result
