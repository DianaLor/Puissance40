def diag_haut(gril,col,lig,j):  
    x1=lig
    y1=col
    x2=lig
    y2=col
    fin=[]
    fin2=[]
    for i in range (6):
        if x1<=5 and y1<=6 and gril[x1][y1]==j: 
                fin.append(gril[x1][y1])
                x1 -= 1
                y1 += 1
    for i in range (6):
        if x2<=5 and y2<=6:
            if gril[x2][y2]==j:
                fin2.append(gril[x2][y2])
                x2 -= 1
                y2 -= 1
    if len(fin) >= 4 or len(fin2)>= 4 :
        return True
    else :
        return False
        
assert diag_haut([[0,2,1,0,1,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,1,2,1,0,2],
                 [0,1,2,1,2,2,0],
                 [0,2,1,0,0,1,0],
                 [2,1,1,2,1,1,0]],0,5,2)==True

assert diag_haut([[0,2,1,1,1,0,0],
                 [0,0,0,1,1,0,0],
                 [0,0,1,2,1,1,2],
                 [0,1,0,1,2,2,1],
                 [0,2,1,0,0,1,0],
                 [2,1,1,2,1,1,0]],6,3,1)==True

assert diag_haut([[0,2,1,0,1,0,0],
                 [0,0,0,1,0,1,0],
                 [0,0,1,2,1,0,2],
                 [0,1,0,1,2,2,0],
                 [0,2,1,0,0,1,0],
                 [2,1,1,2,1,1,0]],2,4,1)==True

assert diag_haut([[0,2,1,0,1,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,1,2,1,0,2],
                 [0,1,0,1,2,2,0],
                 [0,2,1,0,0,1,0],
                 [2,1,1,2,1,1,0]],2,4,1)==False
