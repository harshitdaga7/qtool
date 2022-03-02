#bash 
import os
q_name = input("enter question name: ")
q_name = 'q_' + q_name
path = 'questions/' + q_name + "/"

n = int(input("enter no of input_files: "))
print('creating')
for i in range(n):
	t = str(i)
	if(i < 10):
		t = "0" + str(i)

	inp = 'input' + t + '.txt'
	out = 'output' + t + '.txt' 
	os.system('touch ' + path + 'input/' + inp)
	os.system('touch ' + path + 'output/' + out)
print('created')