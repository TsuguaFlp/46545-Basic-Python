def calc_tip(bill, tip_pct, people):
    total_tip = bill * (tip_pct / 100)
    total = bill + total_tip
    per_person = total / people
    return per_person

bill = float(input("Enter the bill amount: "))
tip_pct = int(input("Enter the tip percentage: "))
people = int(input("Enter the number of people: "))

per_person = calc_tip(bill, tip_pct, people)

print(f"Each person pays: {per_person:.2f}")