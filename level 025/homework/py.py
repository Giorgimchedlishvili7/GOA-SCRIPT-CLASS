score = int(input("Enter the score "))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

    
temp = int(input("Enter the temperature in Celsius: "))


if temp < 0:
    print("Cold ")
elif temp <= 30:
    print("Normal ")
else:
    print("Hot ")

