class Person:
	def hello(self):
		print('Hello word')

p = Person()
p.hello()

#obj.method() == cls.method(obj)
#При вызове метода класса ему передается ссылка на объект. 
#Находясь внутри метода можно получить доступ к этой ссылке через self.
