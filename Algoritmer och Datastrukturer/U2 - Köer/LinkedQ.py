class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedQ:
	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, x):
		new = Node(x)
		if self.isEmpty():
			self.last = new
			self.first = new
		else:
			if self.first.next == None:
				self.first.next = new
			self.last.next = new
			self.last = new
	def dequeue(self):
		if not self.isEmpty():
			value = self.first.value
			self.first = self.first.next
			return value
		return False

	def isEmpty(self):
		return self.first == None

