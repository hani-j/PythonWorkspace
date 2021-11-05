# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " ") # end : 줄바꿈을 하지 않고 " " 이렇게 하겠다
    for lang in language: # lang 변수를 설정하고 language 만큼 출력
        print(lang, end=" ")
    print() # 줄바꿈

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")