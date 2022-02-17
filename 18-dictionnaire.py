
"""creation de dictinnaire dico={} ou {cle:valeur}

acces dico : dico[cle]

ajoute au dico : dico[cle]=valeur

supression dico : dico.pop(cle)
                  del dico[cle]



"""

dico={"prenom":"toto"}

print(dico["prenom"])

dico2 = dico.copy()
dico["chien"]="c est un mammifere"


print(dico)
print(dico2)
for k,v in dico.items(): # .key et .values
    print( "cle {} valeur {}".format(k,v))
    
    
def mafonctoin(**parametres): # une * non nommee ** il doi ettre nomme
    print(parametres)
    
mafonctoin(p=150,ok="blabla")