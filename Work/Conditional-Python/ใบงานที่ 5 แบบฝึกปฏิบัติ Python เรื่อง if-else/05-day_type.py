day = int(input('Enter a day (1-7): '))
if day < 1 or day > 7:
    print("Invalid day. Please enter a number from 1 to 7.")
elif 1 <= day <= 5:
    print("Weekday")
else:
    print("Weekend")