def is_password_good(password):
    has_capital = False
    has_lowercase = False
    has_a_number = False
    if len(password) >= 8:
        for char in password:
            if char.isupper():
                has_capital = True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_a_number = True

    if has_capital and has_lowercase and has_a_number:
        return True
    else:
        return False
txt = input()
print(is_password_good(txt))