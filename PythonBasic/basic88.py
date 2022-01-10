a, d, n = input().split()

s = int(a)
d = int(d)
n = int(n)

while n > 1:
	s += d
	n -= 1
print(s)