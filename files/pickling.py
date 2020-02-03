import pickle

shoplistfile = 'shoplist.data'
shoplist = ['яблоки', 'манго', 'морковь']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
