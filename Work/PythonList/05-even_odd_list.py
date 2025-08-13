n = int(input())
numbers = [int(input()) for _ in range(n)]

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]

print(f"เลขคู่: {even}")
print(f"เลขคี่: {odd}")