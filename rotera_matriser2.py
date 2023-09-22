matris = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for rad in matris:
    print(rad)

rotera_matris = list(list(i) for i in zip(matris[0][::-1], matris[1][::-1], matris[2][::-1]))

omgjord = list(rotera_matris)

for rad in omgjord:
    print(rad)

reversed_1= list(reversed(omgjord)) 
print()
for rad in reversed_1:
    print(rad)