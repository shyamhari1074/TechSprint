def longest_unique_substring(s):
    max_length = 0
    current_substring = ""
    for char in s:
        if char not in current_substring:
            current_substring += char
            max_length = max(max_length, len(current_substring))
        else:
            current_substring = char
    return max_length
