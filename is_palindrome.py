def is_palindrome(text):
    chars_to_remove = ",.!?- "
    for char in chars_to_remove:
        text = text.replace(char, "")
    text_copy = text[::-1]
    if text.lower() == text_copy.lower():
        return True
    else:
        return False
txt = input()
print(is_palindrome(txt))