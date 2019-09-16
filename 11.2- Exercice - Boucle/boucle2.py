# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]
taille = len(B)

def tri(tab):
    for i in range(1, taille):
        j = i-1
        d = tab[i]
        while j>=0 and tab[j] > d:
            tab[j+1] = tab[j]
            j = j - 1
        tab[j+1] = d
    print(tab)

tri(B)
