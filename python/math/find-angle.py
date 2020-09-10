import math

ab = int(input())
bc = int(input())

angle = math.degrees(math.atan2(ab, bc))
angle = int(round(angle))

print(str(angle)+'°')
