t = []
for i in range(11):
	t.append([])
	for j in range(11):
		t[i].append([])

for i in range(1, 11):
	a = input().split()
	for j in range(1, 11):
		t[i][j] = int(a[j-1])
	
x = 2
y = 2
while True:
	if t[x][y] == 2:
		t[x][y] = 9
		break
	t[x][y] = 9
	if t[x][y + 1] == 1:
		x += 1
	else:
		y += 1

for i in range(1, 11):
	for j in range(1, 11):
		print(t[i][j], end=' ')
	print()