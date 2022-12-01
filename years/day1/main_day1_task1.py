import sys

__author__ = "Flederossi"

def main(data):
	splitted = data.split("\n")

	maximum = 0
	count = 0

	for element in splitted:
		if element == "":
			maximum = max([maximum, count])
			count = 0
		else:
			count += int(element)
	
	print(maximum)

if __name__ == "__main__":
	with open(sys.argv[1], "r") as f:
		main(f.read())