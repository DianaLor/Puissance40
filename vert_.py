def vert(gril,j,col,lig) :
    m03=[]
    m14=[]
    m25=[]
    l=[]
    u=1
    drapeau=False
    if j==1:
        u=2
    else:
        u=1
    if gril[lig][col]==j:
        for i in range(6):
            l.append(gril[i][col])
        for t in range(4):
            m03.append(l[t])
        for v in range(1,5):
            m14.append(l[v])
        for o in range(2,6):
            m25.append(l[o])
    
        if u not in m03 and 0 not in m03 and drapeau==False:
                drapeau=True
                    
        if u not in m14 and 0 not in m14 and drapeau==False:
                drapeau=True
                    
        if u not in m25 and 0 not in m25 and drapeau==False:
                drapeau=True
                    
    return drapeau
    
        
assert vert([[0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 1, 2, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 2, 2, 0, 0, 0, 0],
     [0, 1, 2, 0, 0, 0, 0]],1,2,3)==False

assert vert([[0, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0],
     [0, 2, 2, 0, 0, 0, 0],
     [0, 1, 2, 0, 0, 0, 0]],1,2,0)==True

assert vert([[0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 1, 2, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 2, 2, 0, 0, 0, 0],
     [0, 1, 2, 0, 0, 0, 0]],2,2,3)==True







