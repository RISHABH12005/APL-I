''' Write a python script to display students’ details who scored highest marks in Chem among all. '''
def chem():
    return max(students, key=lambda s: s["Chem"])
print("Highest in Chemistry:",chem())
