
number = input("Enter the Armstrong number: ")
digit1 = number[0:1]
digit2 = number[1:2]
digit3 = number[-1]
new_number = (int(digit1)**3) + (int(digit2)**3) + (int(digit3)**3)
number = int(number)
if number == new_number:
    print("Its an Armstrong number")
else:
    print("Its not an Armstrong number")