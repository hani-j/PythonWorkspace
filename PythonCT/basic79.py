n = int(input())
h = 0

for i in range(1, n):
	h += i
	if h >= n:
		print(i)
		break
	i += 1

# n = int(input())

# s = 0
# t = 0
# while s<n :
#   t = t+1
#   s = s+t
  
# print(t)