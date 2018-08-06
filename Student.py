class Student:
	def __init__(self, name, major, gpa):
		self.name = name
		self.major = major
		self.gpa = gpa

	def __repr__(self):
		return f'{self.name}: {self.gpa}'

	def get_gpa(self):
			return self.gpa

student_objects = [
	Student("Joe Smith", "physics", 3.7),
	Student("Jane Jones", "chemistry", 3.9),
	Student("Zoe Grimwald", "literature", 3.8)
	]

print(sorted(student_objects, key=Student.get_gpa))

print(min(student_objects, key=Student.get_gpa))
print(max(student_objects, key=Student.get_gpa))
