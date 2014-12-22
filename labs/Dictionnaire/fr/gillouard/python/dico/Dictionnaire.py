class Dictionnaire:
    """ Classe définissant un dictionnaire avec clé, valeur qui peut être ordonné caractérisée par :
    - une liste de cle
    - une liste de valeur
    Il y a unicité stricte entre les clés et les valeurs"""
    
    def __init__(self, base={}, **donnees):
        """ Constructeur """
        self._keys = []
        self._values = []
        
        # On récupère les données de 'base'
        for cle in base: 
            self[cle] = base[cle]

        # On récupère les données de 'donnees'
        for cle in donnees: 
            self[cle] = donnees[cle]
            
    def __delitem__(self, key):
        """ Suppression d'une entree dans le dictionnaire """
        if key in self._keys:
            indice = self._keys.index(key, 0)
            del self._keys[indice]
            del self._values[indice]
    
    def __getitem__(self, key):
        """Cette méthode spéciale est appelée quand on fait objet[index] """
        if key in self._keys:
            return self._values[self._keys.index(key, 0)]
    
    def __setitem__(self, key, value):
        """ Cette méthode est appelée quand on écrit objet[index ] = valeur """
        if key in self._keys :
            self._values[self._keys.index(key, 0)] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __len__(self):
        """ Retourne la taille du dictionnaire """
        return len(self._keys)
    
    def __repr__(self):
        """ Affiche le contenu du dictionnaire """
        if len(self._keys) > 0:
            chaine = "{" 
            for idx, key in enumerate(self._keys):
                chaine += " " + key + " : " + str(self._values[idx]) + ","
            return chaine[0:len(chaine) - 1] + "}"
        else:
            return "{}"
    
    def reverse(self):
        """ Inverse le dictionnaire """
        self.sortReverse(True)
    
    def sortReverse(self, reverse):
        """ Fonction permettant de trier le dictionnaire """
        tmpKeys = self._keys[:]
        tmpValues = self._values[:]
        if reverse == True:
            self._keys.reverse()
        else:
            self._keys.sort()
        for idx, key in enumerate(self._keys):
            self._values[idx] = tmpValues[tmpKeys.index(key, 0)]
        
    def sort(self):
        """ Trie le dictionnaire """
        self.sortReverse(False)
                
        
    def __iter__(self) :
        """ Sucharge de l'iteration """
        return iter(self._keys)
    
    def keys(self):
        """ Renvoie les cles """
        return list(self._keys)
    
    def values(self):
        """ Renvoie les valeurs """
        return list(self._values)
    
    def items(self):
        """"Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self.keys()): 
            valeur = self.values()[i]
            yield (cle, valeur)

    def __add__(self, dictionnaire_a_ajouter):
        """ Ajout un dictionnaire au dictionnaire courant"""
        nouveau = Dictionnaire()
        for key in self.keys():
            nouveau[key] = self[key]
        
        for key in dictionnaire_a_ajouter.keys():
            nouveau[key] = dictionnaire_a_ajouter[key]
        
        return nouveau
