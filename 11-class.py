#class et attribut

class Humain:
    
    humains_crees = 0
    
    def __init__(self, cprenom="sans Nom", cage=1):
        print("creation humain")
        self.prenom = cprenom
        self.age = cage
        Humain.humains_crees += 1

print("lancement programme")

h1 = Humain("toto", 15)
print("prenom {}".format(h1.prenom))

h2 = Humain("titi", 25)

