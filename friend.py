# ************************ Friiendship Calculator ************************
print(" WELCOME TO THE Friendship CALCULATOR ")
print("-----------------------------------")

name1 = input("Enter your name: ")
name2 = input("Enter her name: ")

score = (sum(ord(c) for c in name1.lower() + name2.lower()) % 51) + 50

print("\nCalculating...")
print(name1, "+", name2)
print("Compatibility:", score, "%")

if score >= 90:
    print(" Perfect match!")
elif score >= 75:
    print(" Something special is definitely there!")
elif score >= 60:
    print(" Good chemistry!")
else:
    print(" Friendship first!")

print("\nResult generated just for fun ")
