# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Version non définitive, du bricolage mais ça marche ! :D

def compteurDeLettre(txt, tab):
    tab[1][0] = txt.count("a")
    tab[1][1] = txt.count("b")
    tab[1][2] = txt.count("c")
    tab[1][3] = txt.count("d")
    tab[1][4] = txt.count("e")
    tab[1][5] = txt.count("f")
    tab[1][6] = txt.count("g")
    tab[1][7] = txt.count("h")
    tab[1][8] = txt.count("i")
    tab[1][9] = txt.count("j")
    tab[1][10] = txt.count("k")
    tab[1][11] = txt.count("l")
    tab[1][12] = txt.count("m")
    tab[1][13] = txt.count("n")
    tab[1][14] = txt.count("o")
    tab[1][15] = txt.count("p")
    tab[1][16] = txt.count("q")
    tab[1][17] = txt.count("r")
    tab[1][18] = txt.count("s")
    tab[1][19] = txt.count("t")
    tab[1][20] = txt.count("u")
    tab[1][21] = txt.count("v")
    tab[1][22] = txt.count("w")
    tab[1][23] = txt.count("x")
    tab[1][24] = txt.count("y")
    tab[1][25] = txt.count("z")
    print(tab[1])

compteurDeLettre(texte, tab_lettres)
