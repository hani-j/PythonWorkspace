index = 1
check = " "
count = 0
from random import *
while index <= 50:
    time = randint(5, 50)
    if time >= 5 and time <= 15:
        check = "O"
        count += 1
    print("[{0}] {1}번째 손님 (소요시간 : {2}분".format(check, index, time))
    check = " "
    index += 1
print("총 탑승 승객 : {0} 분".format(count))    