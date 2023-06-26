import sys
sys.path.append("../ex00")
from ex00 import get_ingot, add_ingot, empty

def split_booty(*purse: dict[str, int]) -> list(dict[str, int]):
	purses = {"gold_ingots":0}
	for dict in purse:
		temp = {}
		if "gold_ingots" in dict:
			temp = get_ingot(dict)
		else:
			temp = add_ingot(temp)
		if temp["gold_ingots"] < 0:
			continue
		purses.update({"gold_ingots" : temp["gold_ingots"] + purses["gold_ingots"]})
	if purses["gold_ingots"] == 0: #yeah,yeah, from checklist
		return ({},{},{})
	if purses["gold_ingots"] % 3 == 0:
		gold_ingots = {"gold_ingots":purses["gold_ingots"] // 3}
		return (gold_ingots, gold_ingots, gold_ingots)
	elif (purses["gold_ingots"] - 1) % 3 == 0:
		gold_ingots = {"gold_ingots":((purses["gold_ingots"]) - 1) // 3}
		return (gold_ingots, gold_ingots, {"gold_ingots":((purses["gold_ingots"]) - 1) // 3 + 1})
	gold_ingots = {"gold_ingots" : (purses["gold_ingots"] - 2) / 3 + 1}
	return (gold_ingots,gold_ingots, {"gold_ingots": (purses["gold_ingots"] - 2) // 3 })


def main():
	print("from subject:",split_booty({"gold_ingots":3},{"gold_ingots":2},{"apples":10}))
	print("one more added",split_booty({"gold_ingots":3},{"gold_ingots":3},{"apples":10}))
	print("prime number:",split_booty({"gold_ingots":3},{"gold_ingots":2},{"gold_ingots":2}))
	print("empty:",split_booty({},{},{}))
	print("combined:",split_booty({},{},{},{},{},{"gold_ingots":3},{"gold_ingots":3},
		{"gold_ingots":3},{"gold_ingots":3},{"gold_ingots":3}))
	print("no gold ingots:",split_booty({"apples":100},{"apples":100},{"apples":100},{"apples":100}))
	print("another empty:",split_booty())
	return 0

if __name__ == "__main__":
	sys.exit(main())