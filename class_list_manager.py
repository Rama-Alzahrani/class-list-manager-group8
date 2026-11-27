# Class List Manager - Group 8
# MIS 211 Bonus Assignment (GitHub Teamwork)
 
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
 
 
# ===== Each student adds her function BELOW this line =====
 
# Rama Alzahrani's function:
def count_names(names):
    return len(names) 
 
# Written by: Sara Zaoui (task 6)
def to_upper(names):
    result = []
    for name in names:
        result.append(name.upper())
    return result

# Written by: Hadeel Aldakheel (task 3,5)
def sort_names(names): # task 3
    return sorted(names, key=lambda name: name.strip().lower())


def names_starting_with(names, letter): # task 5
    if not letter:
        return []
    target = letter.strip().lower()[0]
    return [name for name in names if name.strip().lower().startswith(target)]
# Written by: Lana Aldraian (task 2)
def search_name(names, name):
    for n in names:
        if n.lower() == name.lower():
            return True
    return False

 
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Upper names:", to_upper(names))
    print("Sorted names:", sort_names(names))
    print("Names starting with A:", names_starting_with(names, "A"))
    print("Is Reem in the list?", search_name(names, "Reem"))

main()
