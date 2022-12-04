__author__ = "Flederossi"

def main(data):
<<<<<<< HEAD
	splitted = [[[int(elve.split("-")[0]), int(elve.split("-")[1])] for elve in line.split(",")] for line in data.split("\n")]

	res = 0
	for pair in splitted:
		for j in range(0, 2):
			if pair[j][0] <= pair[-j+1][1] and pair[j][0] >= pair[-j+1][0] and pair[j][1] <= pair[-j+1][1] and pair[j][1] >= pair[-j+1][0]:
				res += 1
				break

	print(res)
=======
	pass
>>>>>>> b09fde1e65c20beca6595d99970a3fef2fee505f

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())