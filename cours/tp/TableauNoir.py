class TableauNoir:
	def __init__(self):
		self.surface = ""

	def ecrire(self, message_a_ecrire):
		if self.surface != "":
			self.surface += "\n"
		self.surface += message_a_ecrire

	def lire(self):
		print(self.surface)

	def effacer(self):
		self.surface = ""
