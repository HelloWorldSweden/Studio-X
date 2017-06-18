class Pokemon:
	def __init__(self, data):
		data = data.strip()		# Remove unneccessary whitespace
		data = data.split(",")	# Convert the data string to a list

		# Add some data about the Pokémon
		self.number = data[1]
		self.name = data[2]
		self.type_primary = data[10]
		self.type_secondary = data[11]
		self.HP = data[3]

	# Function to return the Pokémon as a string
	def __str__(self):
		return self.number + ": " + self.name + "(" + self.HP + ")"

	# Function to return the type of the pokemon in a human readable format
	def getType(self):
		if self.type_secondary != "":
			return self.name + " is primary of type " + self.type_primary + " and secondary of type " + self.type_secondary
		return self.name + " is of type " + self.type_primary

	# Function to update HP for Pokémon
	def updateHP(self, newHP):
		self.HP = newHP

	# Getter function for the name attribute
	def getName(self):
		return self.name

# A list for our pokedex
pokedex = []

# Function to search for a specific Pokémon in the pokedex
def find_pokemon(pokedex, name):
	for p in pokedex:
		if p.getName() == name:
			return p

	return False

# Main function - populate the pokedex from a csv file
def main():
	with open("pokedex.csv", encoding="utf8") as file:
		titlerow = file.readline() 			# First line only contains info about the data fields
		for data in file.readlines(): 		# Loop through the rest of the lines of the file
			p = Pokemon(data) 				# Create Pokemon object from data string
			pokedex.append(p) 				# Add the Pokemon to the pokedex

	while True:
		pokemon = input("Which Pokémon do you want to search for?")
		found = find_pokemon(pokedex, pokemon) 	# Search for Pokémon

		# Print out search results
		if found:
			print(found)
		else:
			print("The Pokémon was not found in the Pokedex")
main()