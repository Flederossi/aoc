__author__ = "Flederossi"

class Monkey:
	def __init__(self, items, operation, test, true, false):
		self.items = items
		self.operation = operation
		self.test = test
		self.true = true
		self.false = false
		self.inspect = 0

def main(data):
	monkeys = []
	splitted = [element.split("\n") for element in data.split("\n\n")]
	for monkey in splitted:
		monkeys.append(
			Monkey(
				[int(item) for item in monkey[1].replace(" ", "").split(":")[1].split(",")],
				monkey[2].replace(" ", "").split("=")[1],
				int(monkey[3].replace(" ", "").split("by")[1]),
				int(monkey[4][-1]),
				int(monkey[5][-1])
			)
		)

	for _ in range(20):
		for monkey in monkeys:
			for item in monkey.items:
				monkey.inspect += 1
				new = eval(monkey.operation.replace("old", str(item)))
				new = new // 3
				if new % monkey.test == 0:
					monkeys[monkey.true].items.append(new)
				else:
					monkeys[monkey.false].items.append(new)
			monkey.items.clear()

	res = []
	for monkey in monkeys:
		res.append(monkey.inspect)
	maxi = max(res)
	del res[res.index(maxi)]
	maxi *= max(res)
	print(maxi)


if __name__ == "__main__":
	with open("input.txt", "r") as f:
		main(f.read())