''' Write a python script to display students’ details who scored highest marks in Phy among all. '''
def phy():
    return max(students, key=lambda s: s["Phy"])
print("Highest in Physics:", phy())
