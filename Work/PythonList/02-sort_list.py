n = int(input())
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)

print(f'ลิสต์เดิม: {lst}')
sorted_lst = sorted(lst)
print(f'ลิสต์เรียงแล้ว: {sorted_lst}')