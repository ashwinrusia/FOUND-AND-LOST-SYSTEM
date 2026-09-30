lost_items = []
found_items = []

def report_lost():
print("\n--- Report Lost Item ---")

```
item = input("Enter item name: ")
description = input("Enter description: ")
location = input("Where did you lose it? ")
date = input("Enter date: ")
name = input("Enter your name: ")
contact = input("Enter contact number: ")

item_details = {
    "item": item,
    "description": description,
    "location": location,
    "date": date,
    "name": name,
    "contact": contact
}

lost_items.append(item_details)

print("Lost item reported successfully!")
```

def report_found():
print("\n--- Report Found Item ---")

```
item = input("Enter item name: ")
description = input("Enter description: ")
location = input("Where did you find it? ")
date = input("Enter date: ")
name = input("Enter your name: ")
contact = input("Enter contact number: ")

item_details = {
    "item": item,
    "description": description,
    "location": location,
    "date": date,
    "name": name,
    "contact": contact
}

found_items.append(item_details)

print("Found item reported successfully!")
```

def show_lost_items():
print("\n--- Lost Items ---")

```
if len(lost_items) == 0:
    print("There are no lost items.")
    return

for i in range(len(lost_items)):
    print("\nItem", i + 1)
    print("Name:", lost_items[i]["item"])
    print("Description:", lost_items[i]["description"])
    print("Location:", lost_items[i]["location"])
    print("Date:", lost_items[i]["date"])
    print("Reported by:", lost_items[i]["name"])
    print("Contact:", lost_items[i]["contact"])
```

def show_found_items():
print("\n--- Found Items ---")

```
if len(found_items) == 0:
    print("There are no found items.")
    return

for i in range(len(found_items)):
    print("\nItem", i + 1)
    print("Name:", found_items[i]["item"])
    print("Description:", found_items[i]["description"])
    print("Location:", found_items[i]["location"])
    print("Date:", found_items[i]["date"])
    print("Found by:", found_items[i]["name"])
    print("Contact:", found_items[i]["contact"])
```

def search_item():
print("\n--- Search Item ---")

```
search = input("Enter item name: ").lower()
item_found = False

for i in range(len(lost_items)):
    if search in lost_items[i]["item"].lower():
        print("\nThis item was reported as LOST.")
        print("Item:", lost_items[i]["item"])
        print("Description:", lost_items[i]["description"])
        print("Location:", lost_items[i]["location"])
        print("Date:", lost_items[i]["date"])
        item_found = True

for i in range(len(found_items)):
    if search in found_items[i]["item"].lower():
        print("\nThis item was reported as FOUND.")
        print("Item:", found_items[i]["item"])
        print("Description:", found_items[i]["description"])
        print("Location:", found_items[i]["location"])
        print("Date:", found_items[i]["date"])
        item_found = True

if item_found == False:
    print("\nNo such item found.")
```

while True:

```
print("\n==============================")
print("      COLLEGE LOST & FOUND")
print("==============================")
print("1. Report Lost Item")
print("2. Report Found Item")
print("3. Show Lost Items")
print("4. Show Found Items")
print("5. Search Item")
print("6. Exit")

choice = input("\nEnter your choice: ")

if choice == "1":
    report_lost()

elif choice == "2":
    report_found()

elif choice == "3":
    show_lost_items()

elif choice == "4":
    show_found_items()

elif choice == "5":
    search_item()

elif choice == "6":
    print("\nThank you for using College Lost & Found!")
    break

else:
    print("\nWrong choice. Please enter a number from 1 to 6.")
```
