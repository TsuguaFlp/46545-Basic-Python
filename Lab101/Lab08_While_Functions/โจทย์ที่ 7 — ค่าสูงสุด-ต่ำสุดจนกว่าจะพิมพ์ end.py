nums = []
while True:
    s = input()
    if s.strip() == "end":
        break
    try:
        nums.append(float(s))
    except ValueError:
        continue

if not nums:
    print("ไม่มีข้อมูล")
else:
    print(f"ค่าสูงสุด: {int(max(nums)) if max(nums).is_integer() else max(nums)}")
    print(f"ค่าต่ำสุด: {int(min(nums)) if min(nums).is_integer() else min(nums)}")