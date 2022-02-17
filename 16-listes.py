
"""liste[x] = affiche element x
liste [-x] = affiche element en partant de la fin

liste [:] = affiche tt les element
liste [:x] = affiche les x premier element
liste [x:] = affiche les x dernier  element

liste [a:b]= affiche les indice a à b (b exclu)

liste.append(element) =ajoute un elem
liste.insert(indice,"element") 
liste.remove("element") ou del liste[indice]

liste.index("element") ->retourne l indice

liste.sort() trier
liste.reverse() trier inverse
liste.count("element") compte le nombre d element

chaine.split(" ") cree un tableau a chak espace
" ".join(liste) cree une phase d une liste

import copy pour copier les listes : liste =copy.deepcopy(listeACopier)

liste1.extend(liste2) concatene la liste


"""

#creation liste
inventaire=["arc", "bouclier","epee"]

for indice, objet in enumerate(inventaire):
    print("indice {} de l objet {}".format(indice,objet))
