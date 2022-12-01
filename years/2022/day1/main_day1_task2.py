__author__ = "Flederossi"

def main(data):
	splitted = data.split("\n")

	splitted.append("")

	ranking = [0, 0, 0]
	count = 0

	for element in splitted:
		if element == "":
			if count > min(ranking):
				ranking[ranking.index(min(ranking))] = count
			count = 0
		else:
			count += int(element)

	res = 0
	for element in ranking:
		res += element

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())