

"""plusieur mode d ouverture : r (lecture seul)
                             : w (ecriture avec remplacement)
                             :a (ecriture avec ajouter a la fin)
                             :x (lecture et ecriture)
                             :r+ (lecture ecriture ds un mm fichier)   

.read =prend tout
.readline =1 ligne par linge
.readlines= le reste des lignes retourn en liste

.write pour ecrire

importer pickle
pickler.Pickler pr enregistrer  et utiliser dump
pickler.Unpickler pr lire et utiliser load

"""

import pickle

class Player:
    def __init__(self,name,level):
        self.name=name
        self.level=level
        
    def whoami(self):
        print("{} : {}".format(self.name,self.level))


with  open("player.data", "rb") as fic:
    get_record=pickle.Unpickler(fic)
    p1=get_record.load()
   

p1.whoami()