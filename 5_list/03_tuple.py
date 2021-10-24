# list와 다르게 추가, 변경 할 수 없음 but. 속도가 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # add 안됨

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)