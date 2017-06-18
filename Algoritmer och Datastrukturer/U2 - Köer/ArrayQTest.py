def main():
	q = ArrayQ()
	q.enqueue(1)
	q.enqueue(2)
	x = q.dequeue()
	y = q.dequeue()
	print(x,y)   # 1 2 ska komma ut
main()