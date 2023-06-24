import sys
import re
import argparse


#redo with argparse module, strip() instead of splitlines?
def printMatchingLines(n):
	i = 0
	for line in sys.stdin.readlines():
		line = line.strip()
		if i >= n:
			break
		if len(line) == 32:
			zeros = re.search('0+.', line).group(0)
			if len(zeros) == 6:
				print(line)
		i += 1

def main():
	try:
		arg = sys.argv[1]
		n = int(arg)
		printMatchingLines(n)
	except Exception as e:
		print("error! wrong input")
	return 0


#OR instead of sys.arg[1] and except
# parser = argparse.ArgumentParser()
# parser.add_argument("number", help="write number of lines to be processed", type = int)
# parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())
		

