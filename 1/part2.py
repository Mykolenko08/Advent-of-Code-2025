a = 1000000000 + 50
zeros = 0
while True:
    move = input("Ln/Rn: ")
    m = int(move[1:])
    for i in range(m):
        if "L" in move:
            a = a - 1
        else:
            a = a + 1
        if a % 100 == 0:
            zeros = zeros + 1
    print(a % 100)
    print(f"Нулів: {zeros}")
