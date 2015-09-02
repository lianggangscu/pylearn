#!/usr/bin/env python
#Filename:pickle.py

'''demostrate how to use pickle module'''
import pickle as p

shoplist = ['apple','pear','rice','fruit','salt']

#open a file and write data into it

f = file('shop.txt','w')
p.dump(shoplist,f)
f.close()

f = file('shop.txt')
store = p.load(f)

print store
