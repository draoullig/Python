import fr.gillouard.python.pendu.fonctions as fct

nom = input("Tapez votre nom : ")

score = 0
scores = {}
scores = fct.getScore()
if scores != None :
    if nom in scores:
        score = scores.get(nom);
else:
    scores ={nom:0}
    
mot = "test"
solution = "*"*len(mot)
essai = 8        
while essai :
    lettre = input("Veuillez saisir une lettre : ")
    pos = mot.split(lettre)
    for idx, letter in enumerate(mot):
        if letter == lettre:
            solution = solution[:idx] + lettre + solution[idx+1:]
    essai = essai - 1        
    if '*' not in solution:
        print("Bien joué, vous avez trouvé le mot : " + solution + " et vous avez gagné " + str(essai) + " points")
        scores[nom] = score + essai
        print("Votre score total est : " + str(scores[nom]))
        fct.putScore(scores)
        essai = 0
    else: 
        print("Vous n'avez pas encore résolu tout le mot : " + solution)
        
    
    

        
    
    