### MinStack Implementation ###

class MinStack:
	
	def __init__(self):
		self.minValue = 0
		self.stack = []

	def push(self,value):
		if len(self.stack) == 0:
			self.minValue = value
		elif value < self.minValue:
			self.stack.append(self.minValue)
			self.minValue = value

		self.stack.append(value)

	def pop(self):
		popedValue = self.stack[-1]
		if self.stack[-1] == self.minValue:
			self.minValue = self.stack[-2]
			del(self.stack[-1])

		del(self.stack[-1])
		return popedValue

	def peek(self):
		print(self.stack[-1])

	def getMin(self):
		print(self.minValue)



minStack = MinStack()
minStack.push(4)
minStack.push(6)
minStack.push(2)
minStack.push(5)
minStack.push(1)
minStack.push(7)

minStack.getMin()
minStack.pop()

minStack.getMin()
minStack.pop()

minStack.getMin()
minStack.pop()

minStack.getMin()



### Lokesh Raj M | Learn In Digital ###
