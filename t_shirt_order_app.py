# Simple T-shirt Ordering Program

# Available options
colors = ["black", "red", "white"]
sizes = ["S", "M", "L", "XL", "XXL"]
cuts = ["male", "ladies"]

orders = [] # List to store all orders

def get_choice(prompt, options):
"""Utility to get a valid choice from user."""
while True:
choice = input(f"{prompt} ({'/'.join(options)}): ").strip().lower()
if choice in [opt.lower() for opt in options]:
return choice
print("❌ Invalid choice, please try again.")

print("👕 Welcome to the T-shirt Order System 👕\n")

while True:
name = input("Enter customer's name: ").strip()
color = get_choice("Choose a color", colors)
size = get_choice("Choose a size", sizes)
cut = get_choice("Choose a cut", cuts)

orders.append({
"name": name,
"color": color,
"size": size.upper(),
"cut": cut
})

more = input("Add another order? (y/n): ").strip().lower()
if more != "y":
break

print("\n📋 Order Summary:")
print("-" * 40)
for i, order in enumerate(orders, 1):
print(f"{i}. {order['name']} — {order['color'].capitalize()} / {order['size']} / {order['cut'].capitalize()}")

print("\n✅ All orders recorded. Thank you!")
