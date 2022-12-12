__author__ = "Flederossi"

def main(data):
	splitted = [list(line) for line in data.split("\n")]
	
	for y in range(len(splitted)):
		for x in range(len(splitted[0])):
			if splitted[y][x] == "S":
				start = (x, y)
				splitted[y][x] = "a"
			elif splitted[y][x] == "E":
				end = (x, y)
				splitted[y][x] = "z"
    
	path = [(0, end)]
	visited = set()
	while True:
		l, pos = path.pop(0)
		if pos in visited:
			continue
		visited.add(pos)
		if splitted[pos[1]][pos[0]] == "a":
			if pos == start:
				print(l)
				break
		
		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			newpos = (pos[0] + dx, pos[1] + dy)
			if 0 <= newpos[1] < len(splitted) and 0 <= newpos[0] < len(splitted[0]) and newpos not in visited and (ord(splitted[pos[1]][pos[0]]) - ord(splitted[newpos[1]][newpos[0]])) <= 1:
				path.append((l+1, newpos))

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())