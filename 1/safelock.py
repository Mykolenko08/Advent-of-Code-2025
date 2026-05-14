a = 50
zeros = 0

while True:
	way = input("Введіть L чи R: ")
	if way == "L":
		m = int(input("Введіть значення (L): "))
		a = a - m
		if a < 0:
			a = a + 100
	else:
		m = int(input("Введіть значення (R): "))
		a = a + m
		if a > 99:
			a = a - 100
	print(a)
	if a == 0:
		zeros = zeros + 1
	print(f"Нулів: {zeros}")