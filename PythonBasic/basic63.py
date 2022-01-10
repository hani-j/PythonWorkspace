a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a >= b) else b)
print(int(c))

# 3항 연산자 : "x if C else y"
# C : True 또는 False를 평가할 조건식 또는 값
# x : C의 평가 결과가 True일 때 사용할 값
# y : C의 평가 결과가 True가 아닐 때 사용할 값