import sys

def add_ingot(purse):
	newPurse = dict(purse)
	if "gold_ingots" in newPurse:
		newPurse.update({"gold_ingots" : purse["gold_ingots"] + 1})
	else:
		newPurse.update({"gold_ingots" : 0})

	return newPurse

def get_ingot(purse):
	newPurse = purse.copy()
	return newPurse

def empty(purse):
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