print("Izvelieties darbibu:")
print("1. Saskaitisana (+)")
print("2. Atnemsana (-)")
choice = input("Izvelies saskaitit vai atnemt(1/2): ")
num1 = float(input("Ievadiet pirmo skaitli: "))
num2 = float(input("Ievadiet otro skaitli: "))

if choice == '1':
    print(f"Rezultats: {num1 + num2}")
elif choice == '2':
    print(f"Rezultats: {num1 - num2}")
else:
    print("-_- megini atkal")