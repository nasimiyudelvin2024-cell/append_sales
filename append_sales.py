# Task 2: Sales Records
product = input("Product name: ")
qty = input("Quantity sold: ")
total = input("Total sales amount: ")

f = open("sales.txt", "a")   # append mode
print(f"{product}, {qty}, {total}", file=f)
f.close()

# Append mode is appropriate because each new sale is added to the end of the
# file without deleting the earlier daily sales records.
print("Sale recorded.")
