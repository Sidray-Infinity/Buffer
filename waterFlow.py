
import numpy as np


if __name__ == "__main__":
    """
    Water can flow from one cell to another if it's height is equal or lower
    left, top -> Pacific
    right, bottom -> Atlantic
    @return : Corrdinate list where both atlantic and pacific water can meet

    """

    mat = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    a = set()
    p = set()

    # Cells where pacific water can reach
    # - Include the border cells first

    bool_mat = []
    for i in range(len(mat)):
        bool_mat.append([False] * len(mat[0]))

    for i in range(len(mat[0])):
        p.add((0, i))

    for i in range(len(mat)):
        p.add((i, 0))
        
    while True:
        temp = []
        # print(np.asarray(bool_mat))
        # print(p)
        # input()
        for point in p:
            x, y = point
            if bool_mat[x][y] == False:
                # print(point)    
                bool_mat[x][y] = True
                val = mat[x][y]
                if y-1 >= 0 and mat[x][y-1] >= val: # up
                    print("(%d, %d) -> (%d, %d) : UP" % (x, y, x, y-1))
                    temp.append((x, y-1))
                if y+1 < len(mat[0]) and mat[x][y+1] >= val: #down
                    print("(%d, %d) -> (%d, %d) : DOWN" % (x, y, x, y+1))
                    temp.append((x, y+1))
                if x-1 >= 0 and mat[x-1][y] >= val: #left
                    print("(%d, %d) -> (%d, %d) : LEFT" % (x, y, x-1, y))
                    temp.append((x-1, y))
                if x+1 < len(mat) and mat[x+1][y] >= val: #right
                    print("(%d, %d) -> (%d, %d) : RIGHT" % (x, y, x+1, y))
                    temp.append((x+1, y))

        for t in temp:
            p.add(t)

        if len(temp) == 0:
            break
    print('\n', np.asarray(bool_mat), '\n')
    # Cells where atlantic water can reach
    print("---------------------------------------------------------------------")
    bool_mat = []
    for i in range(len(mat)):
        bool_mat.append([False] * len(mat[0]))

    for i in range(len(mat[0])):
        a.add((len(mat)-1, i))

    for i in range(len(mat)):
        a.add((i, len(mat[0])-1))
        
    while True:
        temp = []
        for point in a:
            x, y = point
            if bool_mat[x][y] == False:
                # print(point)    
                bool_mat[x][y] = True
                val = mat[x][y]
                if y-1 >= 0 and mat[x][y-1] >= val: # up
                    print("(%d, %d) -> (%d, %d) : UP" % (x, y, x, y-1))
                    temp.append((x, y-1))
                if y+1 < len(mat[0]) and mat[x][y+1] >= val: #down
                    print("(%d, %d) -> (%d, %d) : DOWN" % (x, y, x, y+1))
                    temp.append((x, y+1))
                if x-1 >= 0 and mat[x-1][y] >= val: #left
                    print("(%d, %d) -> (%d, %d) : LEFT" % (x, y, x-1, y))
                    temp.append((x-1, y))
                if x+1 < len(mat) and mat[x+1][y] >= val: #right
                    print("(%d, %d) -> (%d, %d) : RIGHT" % (x, y, x+1, y))
                    temp.append((x+1, y))
            
        for t in temp:
            a.add(t)

        if len(temp) == 0:
            break

    print('\n', np.asarray(bool_mat), '\n')
    print(bool_mat[1][3])
    # Return the intersection of these cells
    print(a.intersection(p))
