import sys

# sample Sets
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Gk1", "Raju", "Gk2", "Nikhil", "Gk3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

# print the sizes of sample Sets
print("Size of Set1: " + str(Set1.__sizeof__()) + "bytes")
print("Size of Set2: " + str(Set2.__sizeof__()) + "bytes")
print("Size of Set3: " + str(Set3.__sizeof__()) + "bytes")
