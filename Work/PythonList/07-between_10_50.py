n = int(input())
numbers = [int(input()) for _ in range(n)]
result = [x for x in numbers if 10 <= x <= 50]
print(f"ค่าที่อยู่ในช่วง 10-50: {result}")