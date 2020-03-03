def victoire(gril,j):
    for y in range(0,6):
        for x in range (0,7):
            if horiz(gril,j,y,x)==True:
                return True
            if vert(gril,j,y,x)==True:
                return True
            if diag_haut(gril,j,x,y)==True:
                return True
            if diag_bas(gril,j,x,y)==True:
                return True
    return False

    
assert victoire([[0,0,1,0,0,0,0],
      [0,0,1,0,0,1,0],
      [1,0,1,2,1,2,0],
      [1,1,1,1,2,2,0],
      [2,2,1,2,1,2,0],
      [2,1,1,1,1,2,2]],2)== True
assert victoire([[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]],1)== False
assert victoire([[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0]],1)== True
