def printMinSubRectangle(M):
    R = len(M) 
    C = len(M[0])  
 
    S = []
    for i in range(R):
        temp = []
        for j in range(C):
            if i == 0 or j == 0:
                temp += M[i][j],
            else:
                temp += 0,
        S += temp,
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                              S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
    min_of_s = S[0][0]
    min_i = 0
    min_j = 0
    for i in range(R):
        for j in range(C):
            if (min_of_s > S[i][j]):
                min_of_s = S[i][j]
                min_i = i
                min_j = j
 
    print("(0,1), (0, 3), (2, 1), (2, 3) ")
    for i in range(min_i, min_i - min_of_s, -1):
        for j in range(min_j, min_j - min_of_s, -1):
            print(M[i][j], end=" ")
        print("")
M = [[1, 0, 0, 1, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [1, 1, 1, 1, 1]]
     
printMinSubRectangle(M)