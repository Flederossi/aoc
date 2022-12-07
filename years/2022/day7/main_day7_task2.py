# This solution is inspired by https://github.com/womogenes

from collections import defaultdict

__author__ = "Flederossi"

def main(data):
	splitted = data.split("\n$ ")
	splitted[0] = splitted[0][2:]

	path = []
	dir_size = defaultdict(int)
	child = defaultdict(list)

	def calc(abspath):
		size = dir_size[abspath]
		for sub in child[abspath]:
			size += calc(sub)
		return size

	for block in splitted:
		lines = block.split("\n")
		command = lines[0]
		outputs = lines[1:]

		command_parts = command.split(" ")
		command_lbl = command_parts[0]

		if command_lbl == "cd":
			argument = command_parts[1]
			if argument == "..":
				del path[-1]
			else:
				path.append(argument)
		elif command_lbl == "ls":
			abspath = "/".join(path)
			sizes = []

			for line in outputs:
				if not line.startswith("dir"):
					sizes.append(int(line.split(" ")[0]))
				else:
					dir_name = line.split(" ")[1]
					child[abspath].append(abspath + "/" + dir_name)
			
			dir_size[abspath] = sum(sizes)

	requ = 30000000 - (70000000 - calc("/"))

	res = 1 << 60
	for abspath in dir_size:
		size = calc(abspath)
		if size >= requ:
			res = min(res, size)

	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())