

#class et attribut

class Humain:
    """classe represente un humain"""
 
    
    def __init__(self, prenom, age):
        print("creation humain")
        self.prenom = prenom
        self._age = age
    
    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("l age n existe pas")
    
    def _setage(self,nouvel_age):
        if nouvel_age < 0:
            self._age=0
        else:
            self._age=nouvel_age
            
    def _delage(self):
        del self._age
        
        
    #property(getter, setter, deleter, helper)  
    age = property(_getage,_setage,_delage, "l age d un humain")

print("lancement programme")

h1 = Humain("toto", 15)
print(h1.age)
del h1.age
print(h1.age)


