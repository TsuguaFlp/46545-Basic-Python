def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

while True:
    print("1. บวกเลขสองจำนวน")
    print("2. ลบเลขสองจำนวน")
    print("3. คูณเลขสองจำนวน")
    print("4. ออก")
    choice = input()
    if choice == '1':
        a = int(input())
        b = int(input())
        print(add(a, b))
    elif choice == '2':
        a = int(input())
        b = int(input())
        print(sub(a, b))
    elif choice == '3':
        a = int(input())
        b = int(input())
        print(mul(a, b))
    elif choice == '4':
        print("จบโปรแกรม")
        break