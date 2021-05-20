age = [64, 63, 37, 28, 4, 7, 7]
family = ["Christine", "Dave", "Mark", "Sarah", "Leah", "Ellie", "Max"]

#using list comprehension to create a dictionary from the lists above.
family_age = {family:age for family, age in zip(family, age)}

print(family_age)
