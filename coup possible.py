def coup_possible(gril, col):
    '''Détermine si possible de jouer dans la colonne col'''
    if 0 in [i[col] for i in gril]:
        return True
    return False
