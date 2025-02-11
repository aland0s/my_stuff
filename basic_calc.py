user_input1, user_input2, user_input3 = int(input()), int(input()), str(input())
if user_input3 == "+":
    print(int(user_input1) + int(user_input2))
elif user_input3 == "-":
    print(int(user_input1) - int(user_input2))
elif user_input3 == "*":
    print(int(user_input1) * int(user_input2))
elif user_input3 == "/":
      if int(user_input2) == 0:
        print("На ноль делить нельзя!")
      else:
          print(int(user_input1) / int(user_input2))
else:
    print("Неверная операция")