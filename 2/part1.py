data = input("Input data: ")

ranges = []

for part in data.split(","):
    part = part.strip()
    if not part:   # skips empty strings
        continue

    start, end = part.split("-")
    ranges.append([int(start), int(end)])

tocheck = []

for start, end in ranges:
    for j in range(start, end + 1):
        tocheck.append(j)

print(tocheck)

invalid = []

for num in tocheck:
    text = str(num)

    if len(text) % 2 == 0:
        half = len(text) // 2

        if text[:half] == text[half:]:
            invalid.append(num)

print("===============")
print(invalid)

sum = 0

for i in range(len(invalid)):
    sum = sum + invalid[i]

print("===============")
print(sum)
