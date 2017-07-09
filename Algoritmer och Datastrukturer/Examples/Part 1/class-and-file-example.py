class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return self.name + "(" + str(self.age) + ")"

def main():
	persons = []
	with open('persondata.txt', encoding="utf8") as file:
		for line in file.readlines():
			line = line.strip();
			data = line.split("|")
			p = Person(data[0], data[1])
			print(p)
			persons.append(p)

main()