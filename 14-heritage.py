"""
isintance (<object>,<classe>) -> verifie l objet qui est bien de la classmethod

issubclass (<class fille>,<classe mere>)-> verifie classe fille et class mere
"""


#class mere
class Vehicule:
    def __init__(self,nom, qte_ess):
        self.nom=nom
        self.ess=qte_ess
    
    def se_deplacer(self):
        print("le vehicule {} se deplace".format(self.nom))    
    
#class fille
class Voiture(Vehicule):
    def __init__(self,nom, qte_ess,puissance):
        Vehicule.__init__(self,nom,qte_ess)
        self.puissance=puissance
        
    def se_deplacer(self):
        print("je roule")
    
class Avion(Vehicule):
    def __init__(self,nom, qte_ess,marchandise):
        Vehicule.__init__(self,nom, qte_ess)
        self.marchandise=marchandise
    
    
#programme prncipal
v1=Voiture("toyota", 80, 420)
v1.se_deplacer()
    
avion1=Avion("f22",2000,"missiles")
avion1.se_deplacer()