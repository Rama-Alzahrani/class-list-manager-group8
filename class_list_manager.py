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


 
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Upper names:", to_upper(names))

 
 
main()
