data_line = str("")
data = str("")
wbreaker = 0
accessable_rolls = 0

pointless = False

row = 138+2 #row lenght + 2 dots on the sides

data = str(data+"#..........................................................................................................................................#")

def check_lu(data, i, row): #left up
	position = i - row - 1
	if data[position] == "@":
		return True
	else:
		return False

def check_u(data, i, row): #up
	position = i - row
	if data[position] == "@":
		return True
	else:
		return False

def check_ru(data, i, row): #right up
	position = i - row + 1
	if data[position] == "@":
		return True
	else:
		return False

def check_l(data, i, row): #left
	position = i - 1
	if data[position] == "@":
		return True
	else:
		return False

def check_r(data, i, row): #right
	position = i + 1
	if data[position] == "@":
		return True
	else:
		return False

def check_ld(data, i, row): #left down
	position = i + row - 1
	if data[position] == "@":
		return True
	else:
		return False

def check_d(data, i, row): # down
	position = i + row
	if data[position] == "@":
		return True
	else:
		return False

def check_rd(data, i, row): # right down
	position = i + row + 1
	if data[position] == "@":
		return True
	else:
		return False


def check_adjacent(data, i, row):
	neighbours = 0
	if check_lu(data, i, row) == True:
		neighbours += 1
	if check_u(data, i, row) == True:
		neighbours += 1
	if check_ru(data, i, row) == True:
		neighbours += 1
	if check_l(data, i, row) == True:
		neighbours += 1
	if check_r(data, i, row) == True:
		neighbours += 1
	if check_ld(data, i, row) == True:
		neighbours += 1
	if check_d(data, i, row) == True:
		neighbours += 1
	if check_rd(data, i, row) == True:
		neighbours += 1
	
	if neighbours >= 4:
		return False
	else:
		return True #accessible


print("Input data lines. 'next' on a blank line - continue to computing")

while wbreaker == 0:
	data_line = input("Input: ")
	if data_line == "next":
		data = str(data+"#..........................................................................................................................................#")
		wbreaker = 1
	else:
		data = str(data+"."+data_line+".")
wbreaker = 0
print(data)

data_list = list(data)


print("Analysis:")
scan_iterations = 0

while wbreaker == 0:
	pointless = True
	for i in range(len(data_list)):
		if data_list[i] == "@":
			if check_adjacent(data_list, i, row) == True: #is accessable
				pointless = False
				accessable_rolls += 1
				data_list[i] = "*"

	if pointless:
		wbreaker = 1
	else:
		scan_iterations += 1	
	print("================")
	print(data_list)
	print("================")
	print(f"Iteration number {scan_iterations}")
	print(f"Rolls accessed and removed: {accessable_rolls}")
