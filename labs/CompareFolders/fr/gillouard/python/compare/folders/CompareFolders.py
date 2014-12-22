""" Outil permettant de comparer le contenu de deux repertoires en effectuant un md5 de tous les fichiers.
    - La liste des fichiers identiques
    - La liste des fichiers presents uniquement dans un des repertoires """

import hashlib
import os, sys
from stat import *
    
def calculateMd5File(full_path):
    """ Fonction calculant le md5 du fichier passe en parametre """
    return hashlib.md5(open(full_path, 'rb').read()).hexdigest()
    
def listFileDir(full_path):
    """Fonction permettant de lister tous les fichiers d'une arborescence"""
    rtn = list()
    for file in os.listdir(full_path):
        # On ne traite pas les fichiers caches
        if  not file.startswith('.'):
            pathname = os.path.join(full_path, file)
            mode = os.stat(pathname)[ST_MODE]
            if S_ISDIR(mode):
                # C'est un repertoire on traite le contenu
                rtn += listFileDir(pathname)
            elif S_ISREG(mode):
                # C'est un fichier on l'ajoute a la liste de resultat
                rtn.append(pathname)
            else:
                # Fichier de type inconnu, on ne le traite pas
                print('Fichier non traite %s', pathname)
    return rtn

def assignFile(dico, list_file):
    """ Fonction permettant d'assigner les fichiers identiques a la meme cle"""
    for e in list_file:
        md5 = calculateMd5File(e)
        #print(md5 + " " + e)
        if md5 in dico:
            dico[md5] = dico[md5] + "," + e
        else:
            dico[md5] = e
    return dico

list1 = listFileDir(sys.argv[1])
print(str(len(list1)) + " fichiers traite dans le repertoire " + sys.argv[1])
dico = assignFile(dict(), list1)
list2 = listFileDir(sys.argv[2])
print(str(len(list2)) + " fichiers traite dans le repertoire " + sys.argv[1])
dico = assignFile(dico, list2)

cpt = 0
uni1 = list()
uni2 = list()
for k in dico:
    if "," in dico[k]:
        cpt +=1
    else:    
        if sys.argv[1] in dico[k]:
            uni1.append(dico[k])
        else:
            uni2.append(dico[k])
            
print("Il y a " + str(cpt) + " fichiers identiques.")
print("Ces " + str(len(uni1)) + " éléments sont uniques dans le rerpertoire " + sys.argv[1])
uni1.sort()
for e in uni1:
    print(e)
print("Ces " + str(len(uni2)) + " éléments sont uniques dans le rerpertoire " + sys.argv[2])
uni2.sort()
for e in uni2:
    print(e)