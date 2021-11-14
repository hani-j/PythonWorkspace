import pickle

with open("profile.pickle", "rb") as profile_file: # profile_file 로 저장
    print(pickle.load(profile_file)) # load 를 통해서 불러와서 출력