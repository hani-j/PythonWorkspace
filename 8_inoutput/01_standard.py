print("Python", "Java") # Python Java
print("Python" + "Java") # PythonJava
print("Python", "Java", sep=",") # Python,Java
print("Python", "Java", "JavaScript", sep=" vs ") # Python vs Java vs JavaScript
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust : 왼쪽 정렬 8칸 확보 / rjust : 4칸 확보 오른쪽 정렬 

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # print("대기번호 : " + str(num))
    print("대기번호 : " + str(num).zfill(3)) # zfill : 3자리, 빈공간은 0으로 채우기

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # str => input : 항상 문자열 형태로 저장
print("입력하신 값은 " + answer + "입니다.")