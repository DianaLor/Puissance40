  
def horiz(gril,lig,col,j):
    '''Détermine si il a un alignement horizontal de 4 pions du joueur j
    où la case (lig,col) appartiendrais '''
    m03=[]
    m25=[]
    m14=[]
    m36=[]
    u=2
    drapeau=False
    if j==1:
        u=2
    else:
        u=1
    if gril[lig][col]==j:
            for r in range(4):
                m03.append(gril[lig][r])
            for k in range(1,5):
                m14.append(gril[lig][k])
            for p in range(2,6):
                m25.append(gril[lig][p])
            for m in range(3,7):
                m36.append(gril[lig][m])
                
            if u not in m03 and 0 not in m03 and drapeau==False:
                drapeau=True
                
            if u not in m14 and 0 not in m14 and drapeau==False:
                drapeau=True
                
            if u not in m25 and 0 not in m25 and drapeau==False:
                drapeau=True
                
            if u not in m36 and 0 not in m36 and drapeau==False:
                drapeau=True
                
    return drapeau

assert horiz([[0, 1, 2, 2, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]],2,2,1)==False

assert horiz([[0, 1, 2, 2, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]],2,2,1)==True


assert horiz([[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]],0,1,2)==False
