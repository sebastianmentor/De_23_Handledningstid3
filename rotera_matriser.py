_3x3 = [[1,2,3],[4,5,6],[7,8,9]]
_4x4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# for row in _3x3:
#     print(row)

for row in _4x4:
    print(row)
print(20*'-')

def rotate_matrix_90_clockwise(matrix):

    N = len(matrix)
    # Antal lager i våran matris vi vill stega genom
    for i in range(N//2):
        # Byta element från index 0 till len(lista)-1 
        for j in range(i, N-i-1):
            # Byter första element med sista så att 1 elemt är rätt position
            matrix[i][j],matrix[j][-i-1] = matrix[j][-i-1],matrix[i][j]
            # Byter ytterligare element från under nedre vänster upp så ett till element är rätt positioin
            matrix[i][j],matrix[-j-1][i] = matrix[-j-1][i],matrix[i][j]
            # Byter de undre element så de 2 sista elementen hamnar rätt och vi har 4 elemet rätt
            matrix[-j-1][i],matrix[-i-1][-j-1] = matrix[-i-1][-j-1],matrix[-j-1][i]
            # Därefter stegar vi ett steg fram och byter nästa 4 element till rätt position
    

rotate_matrix_90_clockwise(_4x4)
for row in _4x4:
    print(row)

# A,B = 3,9
# print(f'{A=}, {B=}')
# A,B = B,A
# print(f'{A=}, {B=}')