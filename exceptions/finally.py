import time

try:
	file = open('poem.txt')
	while True:
		line = file.readline()
		print(line, end='')
		if len(line) == 0:
			break
		time.sleep(2)
except KeyboardInterrupt:
	print('!! чтение файла отменено')
finally:
	file.close()
	print('Закрытие файла')
