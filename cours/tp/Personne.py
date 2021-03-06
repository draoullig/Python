class Personne:

	def __init__(self, nom, prenom):
		self.nom = nom
		self.prenom = prenom
		self.age = 33
		self._lieu_residence = "Paris"

	def _get_lieu_residence(self):
		print("On accède à l'attribut lieu_residence !")
		return self._lieu_residence

	def _set_lieu_residence(self, nouvelle_residence):
		print("Attention, il semble que {} déménage à {}.".format(self.prenom, nouvelle_residence))
		self._lieu_residence = nouvelle_residence

	lieu_residence = property(_get_lieu_residence, _set_lieu_residence)
