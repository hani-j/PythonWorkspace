n = int(input())
s = 0
i = 1

while True:
	s += i
	i += 1
	if s >= n:
		break
print(s)