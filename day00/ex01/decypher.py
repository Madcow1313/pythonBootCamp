import sys

def main():
	try:
		inputString = sys.argv[1]
		listString = inputString.split()
		resultString = ""
		for word in listString:
			resultString += word[0]
		print(resultString)
	except Exception as e:
		print("error! something went wrong:")
		print(e)
	return 0



if __name__ == "__main__":
	sys.exit(main())