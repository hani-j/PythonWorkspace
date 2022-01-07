h, w = input().split()

t = []
for i in range(int(h)+1):
	t.append([])
	for j in range(int(w)+1):
		t[i].append(0)

n = int(input())
for i in range(n):
	l, d, x, y = input().split()
	d = int(d)
	x = int(x)
	y = int(y)
	if d == 0:
		for j in range(int(l)):
			t[x][y] = 1
			y += 1
	else:
		for j in range(int(l)):
			t[x][y] = 1
			x += 1

for i in range(1, int(h)+1):
	for j in range(1, int(w)+1):
		print(t[i][j], end=' ')
	print()