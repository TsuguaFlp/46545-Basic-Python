def show_table(n, limit):
    i = 1
    while i <= limit:
        print(f"{n} x {i} = {n * i}")
        i += 1

n = int(input())
limit = int(input())
show_table(n, limit)