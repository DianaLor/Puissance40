def match_nul(gril):
    '''renvoie True si la partie est nulle, ctd la ligne du haut est remplie'''
    if 0 not in gril[0]:
        if victoire(gril,1)==False and victoire(gril,2)==False:
            return True
        else:
            return False
