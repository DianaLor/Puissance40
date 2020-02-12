def affiche(gril):
    '''affiche une grille de 6 lignes et 7 colonnes
    représente chaque pion des différents joueurs'''
    print("  0","1","2","3","4","5","6")
    compteur = 5 
    for i in gril:
        print(compteur, end="")
        compteur -= 1
        for j in i:
            if j==0:
                print("|.", end="")
            elif j==1:
                print("|x",end="")
            elif j==2:
                print("|0", end="")
        print("|")