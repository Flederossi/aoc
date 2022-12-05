__author__ = "Flederossi"

def main(data):
	splitted = data.split("\n")

	tempcrates = [splitted[i].replace("   ", "[-]").replace(" ", "").split("][") for i in range(0, splitted.index("") - 1)]
	moves = [splitted[i].split(" ") for i in range(splitted.index("") + 1, len(splitted))]

	for i in range(len(tempcrates)):
		tempcrates[i][0] = tempcrates[i][0][1:]
		tempcrates[i][-1] = tempcrates[i][-1][:-1]

	crates = [[] for i in range(len(tempcrates[0]) - 1)]
	for i in range(len(tempcrates) - 1, -1, -1):
		for j in range(0, len(tempcrates[0]) - 1):
			if tempcrates[i][j] != "-":
				crates[j].append(tempcrates[i][j])

	keywords = ["move", "from", "to"]
	for i in range(len(moves)):
		for word in keywords:
			moves[i].remove(word)

	for move in moves:
		column1 = int(move[1]) - 1
		column2 = int(move[2]) - 1
		for element in crates[column1][-int(move[0]):]:
			crates[column2].append(element)
		del crates[column1][-int(move[0]):]

	res = ""
	for stack in crates:
		res += stack[-1]
	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())