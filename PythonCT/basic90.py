a, m, d, n = input().split()

s = int(a)
m = int(m)
d = int(d)
n = int(n)

while n > 1:
	s = s * m + d
	n -= 1
print(s)