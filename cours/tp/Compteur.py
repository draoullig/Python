class Compteur:
	objets_crees = 0
	def __init__(self):
		Compteur.objets_crees += 1
	def combien(cls):
		print("Jusqu'à présent, {} objets ont été créés.".format(cls.objets_crees))
	combien = classmethod(combien)
