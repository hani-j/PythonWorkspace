# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 갯수 + "!"로 구성
#                 (nav)               (5)             (1)       (!)
# 예) 생성된 비빌번호 : nav51!

address = "http://naver.com"
ex = address[7:12]
first = ex[:3]
sum = len(ex)
enum = address.count("e")
print("생성된 비밀번호 : %s%s%s%s" % (first, sum, enum, "!"))
print(f"생성된 비밀번호 : {first}{sum}{enum}!")
# print("생성된 비밀번호 : {first}{sum}{enum}!".format(first = ex[:3], sum = len[ex], enum = address.count("e")))

url = "http://naver.com"
my_str = url.replace("http://", "")
by_str = my_str[:my_str.index(".")] # .이 나오는 위치 까지 
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))