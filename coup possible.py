def coup_possible(gril, col):
    if 0 in [i[col] for i in gril]:
        return True
    return False