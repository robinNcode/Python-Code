lTiles = int(input())
cTiles = int(input())

sum = lTiles * cTiles
sum = sum + ((lTiles - 1) * (cTiles - 1))

print(sum)
sum = 0

sum = sum + (lTiles - 1) * 2
sum = sum + (cTiles - 1) * 2

print(sum)