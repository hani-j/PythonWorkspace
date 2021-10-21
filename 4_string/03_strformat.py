python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 0번째가 대분자가 맞는지 맞으면 true
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n") # n의 위치
print(index)
index = python.index("n", index + 1) # 두번째 n의 위치
print(index)

print(python.find("Java")) # 없는 문자 : -1
# print(python.index("Java")) # 오류가 남
print("hi")

print(python.count("n")) # n의 개수