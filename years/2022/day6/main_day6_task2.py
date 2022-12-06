__author__ = "Flederossi"

def main(data):
	for i in range(14, len(data)):
		check = True
		for j in range(97, 123):
			if data[i-14:i].count(chr(j)) > 1:
				check = False
				break
		if check:
			print(i)
			break


if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())