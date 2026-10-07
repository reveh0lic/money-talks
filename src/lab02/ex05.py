def row_sums(mat):
    if not mat:
        return []

    n=len(mat[0])

    for row in mat:
        if len(row)!=n:
            raise ValueError

    a2=[]
    for row in mat:
        a2.append(sum(row))

    return a2