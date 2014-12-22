import pickle
import os

def getScore():
    if os.path.exists('score.bin'):
        with open('score.bin', 'rb') as fichier :
            mon_depickler = pickle.Unpickler(fichier)
            return mon_depickler.load()

def putScore(scores):
    with open('score.bin', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(scores)
    