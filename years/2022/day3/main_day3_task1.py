__author__ = "Flederossi"

def main(data):
	splitted = [list(set(line[0:int(len(line)/2)]).intersection(line[int(len(line)/2):len(line)]))[0] for line in data.split("\n")]

	res = 0
	for element in splitted:
		s = [38, 96]
		res += ord(element) - s[int(ord(element) >= 97)] 

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())