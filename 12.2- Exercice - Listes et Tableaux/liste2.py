# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

def chercheValMax(tab, colonne = 4, ligne = 3):

    PosX = 0
    PosY = 0
    valeurOld = 0
    valeurMax = 0
    for i in range(0, ligne+1):

        for j in range(0, colonne+1):
            valeurOld = tab[i][j]
            if valeurMax < valeurOld:
                valeurMax = valeurOld
                PosX = i
                PosY = j
        #Je n'arrive pas à mettre le print en dehors de la première boucle et donc à faire remonter l'information du valeurMax afin d'éviter la répétition...
        print("La valeur maximum est : ", valeurMax, "et elle se trouve à l'indice [ ", PosX, " ] [ ", PosY, " ]")


chercheValMax(tab)
