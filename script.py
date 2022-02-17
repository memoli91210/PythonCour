#coding:utf-8

# c est 1 commentaire
import includes.player as player

def dire(nomPersonne="toto", messeagePersonne="hello"):
    print("bjr {} ,{}".format(nomPersonne, messeagePersonne))
    
dire("toto","eh toi")

player.parler("toto","bjr")

def calculerSomme(nbr1,nbr2):
    return nbr1+nbr2

print(calculerSomme(10,5))