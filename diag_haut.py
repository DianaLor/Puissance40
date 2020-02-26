def diag_haut(gril,j,lig,col):
    x1=lig
    y1=col
    x2=lig
    y2=col
    fin=[]
    fin2=[]
    for i in range (6):
        if gril[x1][y1]==j and x1<=5 and y1<6:
            fin.append(gril[x1][y1])
            x1 -= 1
            y1 += 1
    for i in range (6):
        if gril[x2][y2]==j and x2<=5 and y2<=6:
            fin2.append(gril[x2][y2])
            x2 -= 1
            y2 -= 1
    if len(fin) >= 4 or len(fin2)>= 4 :
        return True
    else :
        return False
    
assert diag_haut([[0,0,1,0,0,0,0],
      [0,0,1,0,0,1,0],
      [1,0,1,0,1,2,0],
      [1,1,1,1,2,2,0],
      [2,2,1,2,1,2,0],
      [2,1,1,1,1,2,0]],1,5,1)== True
assert diag_haut([[0,0,1,0,0,0,0],
      [0,0,1,0,0,1,0],
      [1,0,1,0,1,2,0],
      [1,1,1,1,2,2,0],
      [2,2,1,2,1,2,0],
      [2,1,1,1,1,2,0]],1,4,2)== True
assert diag_haut([[0,0,1,0,0,0,0],
      [0,0,1,0,0,1,0],
      [1,0,1,0,1,2,0],
      [1,1,1,1,2,2,0],
      [2,2,1,2,1,2,0],
      [2,1,1,1,1,2,0]],2,4,3)== False
