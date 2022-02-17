#class et attribut

class Humain:
    
    lieu_habitation="terre"
    
    def __init__(self, cprenom, cage):
        print("creation humain")
        self.prenom = cprenom
        self.age = cage
   
        
    def parler(self, message):
        print("l humain {} dit {}".format(self.prenom,message))
        
    def changer_planete(cls, new_planet):
        Humain.lieu_habitation= new_planet
        
    changer_planete=classmethod(changer_planete)
    
    def definition():
        print("l humain est classe comme le meilleur de l univer")
        
    definition=staticmethod(definition)

print("lancement programme")

h1 = Humain("toto", 15)

h1.parler("hey, toi")
print("planete actuel {}".format(Humain.lieu_habitation))

Humain.changer_planete("Mars")

Humain.definition()

print("planete actuel {}".format(Humain.lieu_habitation))



