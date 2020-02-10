def jouer(gril,j,col):
    m=[i[col] for i in gril]
    ligne=0
    drapeau=True
    gril=gril[::-1]
    if coup_possible(gril, col)==True:
        for i in gril:
            if i[col]==0:
                ligne=i
                if j==2 and drapeau==True:
                    ligne[col]=2
                    drapeau=False
                elif j==1 and drapeau==True:
                    ligne[col]=1
                    drapeau=False
        return gril[::-1]
    else:
        return False
