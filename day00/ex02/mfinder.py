import sys
import re

def parseLines(n, line):
	if n == 1 and re.search("\*(?!\*).{3}\*", line):
		return True
	elif n == 2 and re.search("\*\*(?!\*).\*\*", line):
		return True
	elif n == 3 and re.search("\*(?!\*).\*(?!\*).\*", line):
		return True
	return False

def main():
	try:
		numOfLines = 0
		with open("m.txt") as f:
			for line in f:
				line = line.strip()
				if numOfLines > 3 or len(line) != 5:
					print("Error")
					return 0
				numOfLines += 1
				if parseLines(numOfLines, line) != True:
					print("False")
					return 0
	except Exception as e:
		print("error! something went wrong:")
		print(e)
		return -1
	print("True")
	return 0

if __name__ == "__main__":
	sys.exit(main())