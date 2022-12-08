__author__ = "Flederossi"

def main(data):
	res = 0
	splitted = [list(element) for element in data.split("\n")]
	visible = [[False for i in range(len(splitted[0]))] for j in range(len(splitted))]

	h = [range(len(splitted)), range(len(splitted) - 1, -1, -1)]
	for element in h:
		for x in range(0, len(splitted[0])):
			maxi = -1
			for y in element:
				if int(splitted[y][x]) > maxi:
					if visible[y][x] == False:
						res += 1
					visible[y][x] = True
					maxi = int(splitted[y][x])

	v = [range(len(splitted[0])), range(len(splitted[0]) - 1, -1, -1)]
	for element in v:
		for y in range(0, len(splitted)):
			maxi = -1
			for x in element:
				if int(splitted[y][x]) > maxi:
					if visible[y][x] == False:
						res += 1
					visible[y][x] = True
					maxi = int(splitted[y][x])

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())