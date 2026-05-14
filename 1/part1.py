a = 50
zeros = 0

while True:
	move = input("Ln/Rn: ")
	m = int(move[1:])
	if "L" in move:
		a = (a - m) % 100
	else:
		a = (a + m) % 100
	print(a)
	if a == 0:
		zeros = zeros + 1
	print(f"Нулів: {zeros}")
