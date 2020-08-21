if __name__ == "__main__":
    
    mat = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    m = len(mat)
    n = len(mat[0])

    max_cols = []
    min_rows = []

    for i in range(m):
        min_rows.append(min(mat[i]))

    for i in range(len(mat[0])):
        Max = - 10 ** 9
        for j in range(len(mat)):
            if mat[j][i] > Max:
                Max = mat[j][i]

        max_cols.append(Max)

    res = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == min_rows[i] and mat[i][j] == max_cols[j]:
                res.append(mat[i][j])
    print(res)