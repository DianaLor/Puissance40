from random import *
def grille():
    return [[0,0,0,0,0,0] for i in range(6)]

def coup_aléatoire(grille,j):
    m=[]
    h=[]
    for i in grille:
        for w in i:
            h.append(w)
    if 0 in h:        
        for i in range(len(grille)):
            for l in range(6):
                if grille[i][l]==0:
                    m.append([i,l])
        rang=randint(0,len(m)-1)
        if j==1:
            grille[m[rang][0]][m[rang][1]]=j
        elif j==2:
            grille[m[rang][0]][m[rang][1]]=j
        return grille
    else:
        return None
print(coup_aléatoire([[0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1],
                      [0, 0, 1, 0, 0, 0],
                      [1, 1, 0, 0, 0, 1]],2))

    
  
        
 

    