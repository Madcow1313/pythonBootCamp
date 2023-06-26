import sys

def add_ingot(purse: dict[str, int]) -> dict[str, int]:
	newPurse = dict(purse)
	if "gold_ingots" in newPurse:
		newPurse.update({"gold_ingots" : purse["gold_ingots"] + 1})
	else:
		newPurse.update({"gold_ingots" : 1})
	return newPurse

def get_ingot(purse: dict[str, int]) -> dict[str, int]:
	newPurse = purse.copy()
	if "gold_ingots" in newPurse and newPurse["gold_ingots"] > 0:
		newPurse.update({"gold_ingots" : newPurse["gold_ingots"] - 1})
	return newPurse

def empty(purse: dict[str, int]) -> dict[str, int]:
	newPurse = purse.copy() #or newPurse = {} or dict({}) etc
	newPurse.clear()
	return newPurse

def	main():
	purse = {
		"gold_ingots" : 0
	}
	print("task example:",add_ingot(get_ingot(add_ingot(empty(purse)))))
	print("empty:",empty(purse))
	print("simple check:",add_ingot(empty(purse)))
	print(add_ingot(add_ingot(add_ingot(purse))))
	return 0

if __name__ == "__main__":
	sys.exit(main())