def transpose(mat):
    if len(mat) == 0:
        return []

    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError

    new_mat = []
    for j in range(first_row_len):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        new_mat.append(new_row)

    return new_mat