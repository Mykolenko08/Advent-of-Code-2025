looping = True
ranges = []

print("Input ranges")

while looping:
    data_line = input("> ").strip()
    if data_line == "":
        looping = False
    else:
        start, end = data_line.split("-")
        ranges.append([int(start), int(end)])
looping = True
while looping:
    data_line = input("> ").strip()
    if data_line == "":
        looping = False



ranges.sort()


merged = []

for start, end in ranges:


    if not merged:
        merged.append([start, end])

    else:

        last_start, last_end = merged[-1]

        if start <= last_end + 1:

            merged[-1][1] = max(last_end, end)

        else:
            merged.append([start, end])

fresh_id_count = 0

for start, end in merged:

    fresh_id_count += (end - start + 1)


print("================")
print("Merged ranges:")

for r in merged:
    print(f"{r[0]}-{r[1]}")

print("================")
print(f"Unique fresh IDs: {fresh_id_count}")