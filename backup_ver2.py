import os
import time
import zipfile

source = ["/home/serewka/node_modules", "/home/serewka/Документы"]
target_dir = "/home/serewka"

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
  os.mkdir(today)
  print('Каталог успешно создан', today)
target = today + os.sep + now + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
  print('Резервная копия успешно создана', target)
else:
  print('Создание резервной копии не удалось!')



