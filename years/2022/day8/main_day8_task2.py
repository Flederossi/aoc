import numpy

__author__ = "Flederossi"

def value_check(i, a, splitted, x, y):
	check = [[y, x + a], [y, x - a], [y + a, x], [y - a, x]]
	return splitted[check[i][0]][check[i][1]]

def main(data):
	splitted = [list(element) for element in data.split("\n")]
	score = 0

	for y in range(len(splitted)):
		for x in range(len(splitted[0])):
			mult = [0, 0, 0, 0]
			ranges = [
				range(1, len(splitted[0]) - x),
				range(1, x + 1),
				range(1, len(splitted) - y),
				range(1, y + 1)
			]
			for i in range(len(ranges)):
				for a in ranges[i]:
					mult[i] += 1
					if splitted[y][x] <= value_check(i, a, splitted, x, y):
						break

			score = max(score, numpy.prod(mult))

	print(score)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())