from LinkedQ import LinkedQ

def main():
	q = LinkedQ()
	cards = input("Ange kortordning:")
	for card in cards.split(" "):
		q.enqueue(int(card))

	while not q.isEmpty():
		# Put top card on bottom
		c = q.dequeue()
		q.enqueue(c)

		# Display next card
		c = q.dequeue()
		print(c, end=" ")

main()

# 7 1 12 2 8 3 11 4 9 5 13 6 10