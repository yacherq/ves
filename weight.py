import time

time.sleep(1)

print("Здравствуйте! Выберите то, что вы хотите узнать:")

time.sleep(1)

answer = int(input("[1]-Рассчитать, сколько калорий мне нужно\n[2]-Рассчитать индекс массы тела\n[3]-Как не допустить ожирения?\n"))

#расчет каллорий
def energy():
	a = int(input("Ваш пол:\n[1]-Мужской\n[2]-Женский\n"))

	def menE():
		vesE = int(input("Введите ваш вес(кг): "))
		rostE = int(input("Введите ваш рост(см): "))
		ageE = int(input("Введите ваш возраст(лет): "))
		finalE = (10 * vesE) + (float(6.25) * rostE) - (5 * ageE) + 5
		print(finalE)

	def womenE():
		veswE = int(input("Введите ваш вес(кг): "))
		rostwE = int(input("Введите ваш рост(см): "))
		agewE = int(input("Введите ваш возраст(лет): "))
		finalwE = (10 * veswE) + (float(6.25) * rostwE) - (5 * agewE) - 161
		print(finalwE)
	
	if a == 1:
		menE()
	if a == 2:
		womenE()



#расчет ИМТ
def imt():
	vesI = int(input("Введите ваш вес(кг): "))
	rostI = int(input("Введите ваш рост(см): "))
	finalI = vesI / (rostI * rostI) * 10000
	print(round(finalI, 2))
	time.sleep(1)
	
	if 18 < finalI < 25:
		print("Ваш ИМТ в норме, все в порядке.")
	if finalI < 18:
		print("Вы слишком мало весите. Задумайтесь о питании!")
	if 19 < finalI < 25:
		print("У вас есть излишний вес.")
	if 25 < finalI < 30:
 		print("У вас предожирение. Задумайтесь о правильном питании!")
	if 31 < finalI < 35:
 		print("У вас первая стадия ожирения!")
	if 36 < finalI < 40:
 		print("У вас вторая стадия ожирения!")
	if finalI > 40:
 		print("У вас третья стадия ожирения!")






if answer == 1:
	energy()
if answer == 2:
	imt()


