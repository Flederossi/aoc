__author__ = "Flederossi"

def main(data):
	d = {
		"R": [1, 0],
		"L": [-1, 0],
		"D": [0, 1],
		"U": [0, -1]
	}

	h_pos = (0, 0)
	t_pos = (0, 0)
	visited = set()

	splitted = [line.split(" ") for line in data.split("\n")]

	for move in splitted:
		for i in range(int(move[1])):
			visited.add(t_pos)
			h_pos = (h_pos[0] + d[move[0]][0], h_pos[1] + d[move[0]][1])
			
			dr = (h_pos[0]-t_pos[0])
			dc = (h_pos[1]-t_pos[1])

			if abs(dr) >= 2:
				t_pos = (h_pos[0] - 1 if t_pos[0] < h_pos[0] else h_pos[0] + 1, h_pos[1])
			elif abs(dc) >= 2:
				t_pos = (h_pos[0], h_pos[1] - 1 if t_pos[1] < h_pos[1] else h_pos[1] + 1)

	print(len(visited))


if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())