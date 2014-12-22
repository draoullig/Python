def table_par_7():
	""" Fonction affichant la table de multiplication par 7"""
	nb = 7
	i = 0
	while i<10:
		print(i + 1, "*", nb, "=", (i + 1) * nb)
		i += 1

help(table_par_7)

table_par_7()
