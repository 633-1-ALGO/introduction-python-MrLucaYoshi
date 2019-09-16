# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cpt = 0
cpt2 = 0
cpt3 = 1
nombre = 1
calcul = 0
suite = []
while len(liste)>cpt:
    print(liste[cpt],end=' ')
    cpt += 1

while 11 > cpt2:
    print(" ", end=' ')
    print(nombre, end=' ')
    while 10 > cpt3:
        calcul = nombre * liste[cpt3]
        suite.append(calcul)
        cpt3 += 1
    print(suite[cpt2])
    nombre += 1
    cpt2 += 1




