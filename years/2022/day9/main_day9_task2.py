__author__ = "Flederossi"

def follow(h, t):
	dr = (h[0]-t[0])
	dc = (h[1]-t[1])

	if abs(dr) >= 2 and abs(dc) >= 2:
		t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1)
	elif abs(dr) >= 2:
		t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1])
	elif abs(dc) >= 2:
		t = (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)

	return t

def main(data):
	d = {
		"R": [1, 0],
		"L": [-1, 0],
		"D": [0, 1],
		"U": [0, -1]
	}

	h_pos = (0, 0)
	t_pos = [(0, 0) for _ in range(9)]
	visited = set()

	splitted = [line.split(" ") for line in data.split("\n")]

	for move in splitted:
		for _ in range(int(move[1])):
			h_pos = (h_pos[0] + d[move[0]][0], h_pos[1] + d[move[0]][1])
			
			t_pos[0] = follow(h_pos, t_pos[0])
			for i in range(1, 9):
				t_pos[i] = follow(t_pos[i-1], t_pos[i])
			visited.add(t_pos[8])

	print(len(visited))


if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())