def victoire(gril,j):
    for lig in range(6):
        for col in range(7):
            if horiz(gril, j, lig, col) == True or vert(gril, j, lig, col) == True or diag_haut(gril, j, lig, col) ==True or diag_bas(gril, j, lig, col)==True:
                n+=1

    if n!=0:
        return True
    else:
        return False


    
assert victoire([[0,0,1,0,0,0,0],
      [0,0,1,0,0,1,0],
      [1,0,1,2,1,2,0],
      [1,1,1,1,2,2,0],
      [2,2,1,2,1,2,0],
      [2,1,1,1,1,2,2]],2,2,3)== True
assert victoire([[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]],1,1,5)== False
assert victoire([[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0]],1,5,3)== True
