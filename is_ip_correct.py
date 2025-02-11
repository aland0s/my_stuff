s = input()
ip = s.split(".")
counter = 0
for octet in ip:
    if 0 <= int(octet) <= 255:
        counter += 1
if counter == 4:
    print("ДА")
else:
    print("НЕТ")
