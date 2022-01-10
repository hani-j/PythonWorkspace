a, r, n = input().split()

s = int(a)
r = int(r)
n = int(n)

while n > 1:
	s *= r
	n -= 1
print(s)