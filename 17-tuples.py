
#creatio de tuple
"""type immuable on ne peu pa modifier

mais en affetation on peu modifier

2 raison d utiliser les tuples : affecttion multiple de variable
                                 retour multiple de fonction
"""

mon_tuple=(45, 64)

def get_player_position():
    posX=50
    posY=100
    return(posX,posY)

#programme
coordX=0
coordY=0


(coordX, coordY)=get_player_position()

coordX=150
coordY=150

print("position joueur{} {}".format(coordX,coordY))