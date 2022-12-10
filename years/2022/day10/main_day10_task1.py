__author__ = "Flederossi"

def main(data):
	x = 1
	check = [20, 60, 100, 140, 180, 220]
	splitted = [line.split(" ") for line in data.split("\n")]
	wait = False
	res = 0

	cm = 0
	for command in splitted:
		if command[0] == "addx":
			cm += 2
		elif command[0] == "noop":
			cm += 1
	
	i = 0
	for c in range(1, cm):
		if c in check:
			res += c * x
		
		if splitted[i][0] == "addx":
			if wait == True:
				x += int(splitted[i][1])
				i += 1
				wait = False
			else:
				wait = True
		elif splitted[i][0] == "noop":
			i += 1

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())