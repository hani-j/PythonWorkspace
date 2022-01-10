n = int(input())
a = input().split()

for i in range(n):
	a[i] = int(a[i])
b = a[0]
for i in range(n-1):
	if b > a[i+1]:
		b = a[i+1]
print(b)