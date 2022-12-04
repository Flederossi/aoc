__author__ = "Flederossi"

def main(data):
	splitted = data.split("\n")
	splitted = [list(set(splitted[i]).intersection(splitted[i+1], splitted[i+2]))[0] for i in range(0, len(splitted), 3)]

	res = 0
	for element in splitted:
		s = [38, 96]
		res += ord(element) - s[int(ord(element) >= 97)] 

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())