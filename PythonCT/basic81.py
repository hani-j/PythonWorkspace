n = input()

if n == 'A':
	n = 10
if n == 'B':
	n = 11
if n == 'C':
	n = 12
if n == 'D':
	n = 13
if n == 'E':
	n = 14
if n == 'F':
	n = 15
for i in range(1, 16):
	print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# print('%X'%n) : n 에 저장되어있는 값을 16진수 형태로 출력