# 여러 모듈 파일을 묶어둔 것

# 방법 1
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# 방법 2
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))