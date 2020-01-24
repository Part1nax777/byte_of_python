class Person:
	def __init__(self, name): #конструктор
		self.name = name

	def hello(self):
		print('Hello', self.name)

p = Person('Swaroop')
p.hello()

