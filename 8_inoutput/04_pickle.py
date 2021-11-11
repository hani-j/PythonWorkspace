# pickle : 데이터를 파일 형태로 저장

import pickle
profile_file = open("profile.pickle", "wb") # b : binary  / pickle에서는 필수
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()