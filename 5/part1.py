looping = True
data_line = ""
ranges_start = []
ranges_end = []
ids = []
range_parts = ""

# inputs

print("Input ranges")

while looping:
	data_line = str(input("> "))
	if data_line == "":
		looping = False
	else:
		range_parts = data_line.split("-")
		ranges_start.append(int(range_parts[0]))
		ranges_end.append(int(range_parts[1]))

looping = True
print("Input IDs")

while looping:
	data_line = input("> ")
	if data_line == "":
		looping = False
	else:
		ids.append(int(data_line))

# =======--------========
# start  -  end
#   3    -  5
#	3	4   5

def id_inrange(ranges_start, ranges_end, target_id):
    for i in range(len(ranges_start)):
        if target_id >= ranges_start[i] and target_id <= ranges_end[i]:
            print(f"{target_id} IS FRESH!!!!!!!!!!!!!!!")
            return 1

    print(f"{target_id} went bad")
    return 0


fresh_count = 0

for i in range(len(ids)):
    fresh_count += id_inrange(ranges_start, ranges_end, ids[i])

print("=========================")
print(f"Found {fresh_count} IDs")