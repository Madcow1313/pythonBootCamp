import sys
sys.path.append("../ex00")
from ex00 import get_ingot, add_ingot, empty

def my_decorator(func):
	def wrapper(*args):
		print("SQUEAK")
		return func(*args)
	return wrapper

get_ingot = my_decorator(get_ingot)
add_ingot = my_decorator(add_ingot)
empty = my_decorator(empty)

def main():
	purse = {"gold_ingots":1}
	print("task example:",add_ingot(get_ingot(add_ingot(empty(purse)))))
	return 0

if __name__ == "__main__":
	sys.exit(main())