import json

__author__ = "Flederossi"

def compare(e1, e2):
	t1 = type(e1)
	t2 = type(e2)
	if t1 is int and t2 is int:
		return e2 - e1
	elif t1 is int and t2 is list:
		return compare([e1], e2)
	elif t1 is list and t2 is int:
		return compare(e1, [e2])
	elif t1 is list and t2 is list:
		for ne1, ne2 in zip(e1, e2):
			val = compare(ne1, ne2)
			if val != 0:
				return val
		return len(e2) - len(e1)

def main(data):
	splitted = [pair.split("\n") for pair in data.split("\n\n")]

	pdiv = [[[2]], [[6]]]
	idiv = [i for i in range(1, len(pdiv) + 1)]
	for i in range(len(splitted)):
		l = [json.loads(splitted[i][0]), json.loads(splitted[i][1])]
		for p in l:
			for j in range(len(pdiv)):
				if (compare(p, pdiv[j])) > 0:
					idiv[j] += 1
	res = 1
	for i in idiv:
		res *= i
	print(res)

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())