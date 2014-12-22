from math import ceil
from random import randrange

def jouer(nb, mise):
	tirage=randrange(50)
	print("Le tirage est :", tirage)
	if tirage == nb :
        	mise = mise * 2
	elif tirage%2 == nb%2:
        	mise = mise + ceil(mise/2)
	else:
        	mise = 0
	return mise

nb=int(input("Veuillez choisir un nombre entre 0 et 49 ?"))
mise=int(input("Veuillez choisir une mise en dollar ?"))
print("Vos gains sont de ", jouer(nb, mise), "$")
