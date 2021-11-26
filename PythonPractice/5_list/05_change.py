# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} 
print(menu, type(menu)) # set : {} 순서 없음, 중복 안됨

menu = list(menu)
print(menu, type(menu)) # list : [] 순서 있음, 중복 가능, 추가 변경 가능

menu = tuple(menu)
print(menu, type(menu)) # tuple : () 추가 변경 안됨, 빠름

menu = set(menu)
print(menu, type(menu))