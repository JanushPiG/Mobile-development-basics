file_in = open("input.txt", "r", encoding="utf-8")

n = {}
roles = []
buffer = file_in.readline()

if "roles:" not in buffer:
	print("error")
	exit(-1)

while True:
	buffer = file_in.readline()
	if "textLines:" in buffer:
		break
	roles += [buffer.rstrip()]

count = 0
key = str(0)

while True:
	buffer = file_in.readline()
	buffer.rstrip()

	if buffer == "":
		break

	temp = buffer.split(":")

	if len(temp) > 1:
		for i in range(0, len(roles), 1):
			if temp[0] == roles[i]:
				key = roles[i]
				count += 1
				break

	if key not in n:
		n[key] = ([str(count) + ") " + buffer])
	else:
		n[key] += ([str(count) + ") " + buffer])

file_in.close()
file_out = open("text_output.txt", "w")

for i in n.keys():
	file_out.write(i + ":\n")
	for z in range(0, len(n[i]), 1):
		file_out.write(n[i][z].replace(i + ":", "", 1))
	file_out.write("\n")
file_out.close()