class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return self.name + "(" + str(self.age) + ")"

def main():
	p = Person("Johan", 23)
	print(p)

main()