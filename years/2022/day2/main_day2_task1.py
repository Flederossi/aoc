__author__ = "Flederossi"

values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

win = [2, 3, 1]

def main(data):
	splitted = [[values[element.split(" ")[0]], values[element.split(" ")[1]]] for element in data.split("\n")]

	res = 0
	for element in splitted:
		res += element[1]
		if win[element[0] - 1] == element[1]:
			res += 6
		elif element[0] == element[1]:
			res += 3

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())