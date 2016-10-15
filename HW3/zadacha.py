number1=input("Напишите первое число. ")
number2=input("Напишите второе число. ")
number3=input("Напишите третье число. ")
if int(number1) + int(number2) == int(number3):
    print("Числа " + number1 + " и " + number2 + " дают в сумме число " + number3 + ".")
else: print("Числа " + number1 + " и " + number2 + " не дают в сумме число " + number3 + ".")
if  int(number1) // int(number2) == int(number3):
    print("Число " + number1 + " при делении на " + number2 + " дает число " + number3 + ".")
else: print("Число " + number1 + " при делении на " + number2 + " не дает число " + number3 + ".")
