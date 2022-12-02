__author__ = "Flederossi"

values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

win = [2, 3, 1]
lose = [3, 1, 2]

def main(data):
	splitted = [[values[element.split(" ")[0]], values[element.split(" ")[1]]] for element in data.split("\n")]

	res = 0
	for element in splitted:
		choose = 0
		if element[1] == 1:
			choose = lose[element[0] - 1]
		elif element[1] == 2:
			choose = element[0]
			res += 3
		else:
			choose = win[element[0] - 1]
			res += 6

		res += choose

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())