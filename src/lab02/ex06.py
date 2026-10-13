def col_sums(mat):
    if not mat:
        return []

    n=len(mat[0])

    for row in mat:
        if len(row)!=n:
            raise ValueError

    a2=[]
    for j in range(n):
        a3=0
        for i in range(len(mat)):
            a3+=mat[i][j]
        a2.append(a3)

    return a2

print(f"col_sums([[1, 2, 3], [4, 5, 6]]) -> {col_sums([[1, 2, 3], [4, 5, 6]])}")