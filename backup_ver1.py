import os
import time

source = ['"/home/serewka/Документы"', "/home/serewka/Изображения"]

target_dir = "/home/serewka/'Рабочий стол'"

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
  print('резервная копия успешно создана в', target)
else:
  print('Создание резервной копии не удалось')
