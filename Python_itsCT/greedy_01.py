n = int(input())
a = n / 500
b = (n % 500) / 100
c = ((n % 500) % 100) / 50
d = (((n % 500) % 100) % 50) / 10
print(int(a) + int(b) + int(c) + int(d))

# // : 몫

# 답안 예시

n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
	count += n // coin
	n %= coin

print(count)
