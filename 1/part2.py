a = 50
zeros = 0

while True:
    move = input("Ln/Rn: ").strip()

    m = int(move[1:])
    old = a

    if move[0] == "L":
        zeros = zeros + (m - old + 99) // 100
        a = (a - m) % 100

    else:
        zeros = zeros + (old + m) // 100
        a = (a + m) % 100

    print(a)
    print(f"Нулів: {zeros}")