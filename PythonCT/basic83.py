# r, g, b = input().split()
# c = 0

# for i in range(int(r)):
# 	for j in range(int(g)):
# 		for k in range(int(b)):
# 			print(i, j, k, end=' ')
# 			print()
# 			c += 1
# print(c)

r, g, b = input().split()

for i in range(int(r)):
	for j in range(int(g)):
		for k in range(int(b)):
			print(i, j, k)
print(int(r)*int(g)*int(b))