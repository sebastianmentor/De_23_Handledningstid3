_3x3 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
_4x4 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]


rotate_3x3 =[list(row) for row in [i for i in zip(*_3x3[::-1])]]

for row in rotate_3x3:
    print(row)