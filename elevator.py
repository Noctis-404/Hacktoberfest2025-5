door = input().strip()
a = int(input())

d = 0 if door == "front" else 1

side = (a == 1) ^ d
print("L" if side else "R")
