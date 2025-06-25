score = int(input("Enter your score (0-100): "))
if 0 <= score <= 100:
    if score >= 80:
        print("You got A")
    elif 75 <= score <= 79:
        print("You got B+")
    elif 70 <= score <= 74:
        print("You got B")
    elif 65 <= score <= 69:
        print("You got C+")
    elif 60 <= score <= 64:
        print("You got C")
    elif 55 <= score <= 59:
        print("You got D+")
    elif 50 <= score <= 54:
        print("You got D")
    else:
        print("You got F")
else:
    print("Invalid score. Please enter a value between 0 and 100.")