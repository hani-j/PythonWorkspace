jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0번째 부터 1번째 까지
print("월 : " + jumin[2:4]) # 2~3
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤 = -1
# # 맨 뒤에서 7번째부터 끝까지 (-7654321)