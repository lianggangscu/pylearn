#!/usr/bin/env python
#Filename:list.py

shoplist = ['apple','mango','carrot','banna']

print('I have %d items to purchase' %(len(shoplist)))

for item in shoplist:
	print(item)

print("I also need buy rice")
shoplist.append('rice')
print('now,the shoplist is ')
print(shoplist)


print("I want to sort the shoplist")
shoplist.sort()
print(shoplist)

print("The first item I want to buy")
print(shoplist[0])

del shoplist[0]
print('I aslo need to buy')
print(shoplist)

