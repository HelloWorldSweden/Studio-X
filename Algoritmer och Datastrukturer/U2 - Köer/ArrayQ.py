from array import array

class ArrayQ:
	def __init__(self):
		self.__queue = array('b')
		self.__count = 0

	def enqueue(self, obj):
		self.__count += 1
		self.__queue.append(obj)

	def dequeue(self):
		self.__count -= 1
		return self.__queue.pop(0)

	def isEmpty(self):
		return self.__count== 0