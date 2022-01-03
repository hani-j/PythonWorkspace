n = int(input(), 16)

for i in range(1, 16):
	print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

	# print("%X * %X = %X"%(n, i, n * i))

# int(a, 16) : a를 17진수로 인식해 변수 n에 저장 - basic29
# format(a, ".2f") : a를 소수점 아래 3번째 자리에서 반올림 한 값