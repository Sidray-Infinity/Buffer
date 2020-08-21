

def hasCommonFactors(a, b):
    i = 2
    while i <= a and i <= b:
        if a%i == 0 and b%i == 0:
            return True
        i += 1
    return False

if __name__ == "__main__":
    """
    - A[i] -> Nodes in the graph
    - Edge b/w A[i] and A[j] exists, if they have a common factor > 1
    @return : size of the largest connected component in the graph
    """
    import numpy as np
    a = [4,6,15,35]
    e = np.zeros((len(a), len(a)), dtype="int32")

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if(hasCommonFactors(a[i], a[j])):
                e[i][j] = 1

    print(e)

    components = []
    visited = [False] * len(a)

    while False in visited:
        component = []

        i = visited.index(False)
        ne = [ele for ele in e[i] if ele == 1]
        component.append(i)

        while len(ne) > 0:
            new_ne = 

        print(ne)
        components.append(component)
        break
