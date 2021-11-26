class Unit:
	def __init__(self):
		print("Unit 생성자")

class Flyable:
	def __init__(self):
		print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): # Unit()
	def __init__(self):
		super().__init__()

class FlyableUnit(Flyable, Unit): # Flyable()
	def __init__(self):
		# super().__init__()
		Unit.__init__(self)
		Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

# 두개 이상의 다중 클래스 상속 => 첫번째만 호출됨
# 그래서 super 대신 하나씩 초기화