def mon_decorateur(fonction):
	""" Premier exemple de décorateur """
	print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
	return fonction

@mon_decorateur
def salut():
	""" Fonction modifiée par notre décorateur """
	print("Salut !")

def mon_decorateur2(fonction):
	""" Notre décorateur : il va afficher un message avant l'appel de la fonction définie """

	def fonction_modifiee():
		""" Fonction que l'on va renvoyer. Il s'agit en fait d'ine verison un peu modifiée de nore fonction originellement définie. On se contente d'afficher un avertissement avant d'exécuter notre fonction originellement définie """
		print("Attention ! On appelle {0}".format(fonction))
		return fonction()
	return fonction_modifiee

@mon_decorateur2
def salut2():
	print("Salut !")

def mon_decorateur3(fonction_origine):
	""" Décorateur levant une exception pour noter que la fonction_origine est obsolète """
	
	def fonction_modifiee():
		raise RuntimeError("la fonction {0} est obsoltète !".format(fonction_origine))
	return fonction_modifiee

@mon_decorateur3
def salut3():
	print("Salut !")
