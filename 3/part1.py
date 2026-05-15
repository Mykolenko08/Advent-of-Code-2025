gen_sum = 0
while True:
	pairs_appended = 0
	pairs_skipped = 0
	bank_input = str(input("Input: "))
	bank = []

	for i in range(len(bank_input)):
		bank.append(bank_input[i])

	print(bank)

	pairs = []

	for i in range(len(bank)):
		for j in range(len(bank)):
			if i >= j:
				pairs_skipped = pairs_skipped + 1
			else:
				pairs.append(int(bank[i]+bank[j]))
				pairs_appended = pairs_appended + 1
	print(pairs)

	max_of_bank = 0

	print(f"Append: {pairs_appended}")
	print(f"Skipped: {pairs_skipped}")

	for i in range(len(pairs)):
		if pairs[i] > max_of_bank:
			max_of_bank = pairs[i]

	print(max_of_bank)
	print(f"Sum: {gen_sum} -> {gen_sum+max_of_bank}")
	gen_sum = gen_sum + max_of_bank
	print("==========")
	print(f"Sum = {gen_sum}")