annee=input("Saisissez une année : ")
try:
	annee = int(annee)
except:
	print("""Erreur lors de la conversion de l'année.""")
bissextile = False
if annee%4 == 0:
	if annee%100 == 0:
		if annee%400 ==0:
			bissextile = True	
		else:
			bissextile = False
	else:
		bissextile = True
	
if bissextile:
	print("""L'année est bissextile""")	
else:
	print("""L'année n'est pas bissextile""")
