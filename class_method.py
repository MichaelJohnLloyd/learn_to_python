#Here I have created the class <person>. This contains a variable which currently is set to 0
class person:
	number_of_people = 0

	#Below is the init function for the class itself. As seen, the data of a person will be run through this
	#function and then the variable above will show +1 for every person added due to the function being called at the end
	#the code
	def __init__(self, name, lastname, age):
		self.name = name
		self.lastname = lastname
		self.age = age
		person.add_person()

	#Class method is a function that only works within a set class. In this instance, the class is person
	@classmethod
	def add_person(cls):
		person.number_of_people += 1

	#This can be called(as seen below) to print out/call the current added people
	@classmethod
	def current_students(cls):
		return cls.number_of_people

	#This function is the base for the class <person>. If the data fits into this class then this will be the default
	#function called
	def responsibilities(self):
		print("I have no responsibilities")

#This new class contains a new responsibility function. We can pass data through this by calling the class with the
#class of <person> as an argument
class manager(person):
	def responsibilities(self):
		print("I manage the workforce")

#This is the same as above, just for another new class
class employee(person):
	def responsibilities(self):
		print("I manage the checkouts")
		
	
#The variables below contain each one of the classes, with the data passed through as the arguments
p = person("Michael", "Lloyd", 33)
m = manager("Samuel", "Detnon", 30)
e = employee("Greg", "Reid", 40)


p.responsibilities()
m.responsibilities()
e.responsibilities()

#The below prints show that you can access the information you need by calling through the init function above using
#the class variables.
print(m.lastname)
print(e.age)
print(person.current_students())
