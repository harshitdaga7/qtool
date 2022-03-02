#update input n and output n for the functions
import os
import sys
def input_gen(n):
	for i in range(n):
		path = "input/input"
		appnd = ""
		if(i < 10):
			appnd = "0"+ str(i) + ".txt"
		else:
			appnd = str(i) + ".txt"

		print('doing test',i)
		os.system('python3 test.py >' + path + appnd + " " + str(i))
		print('completed test',i)


def output_gen(n):
	for i in range(n):
		path = "output/output"
		appnd = ""
		if(i < 10):
			appnd = "0"+ str(i) + ".txt"
		else:
			appnd = str(i) + ".txt"
		print('doing test',i)
		os.system('./solution.out < input/input' + appnd + " >" + path + appnd)
		print('completed test',i)


def main():
	try:
		a = sys.argv[1]
		t = 11
		if(a == 'in'):
			input_gen(t)
		elif (a == 'out'):
			output_gen(t)
		else:
			print('no argument given')
	except Exception as e:
		print(e)
		print('type argument "in" or "out"')


# main()

