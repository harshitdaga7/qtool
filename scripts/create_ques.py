#bash commands
import os
import shutil

question_name = input("Type question name: ")
question_name = "q_" + question_name
tch_cmd = ['question.txt','question.md','editorial.txt','editorial.md','comments.txt','solution.cpp','solution.py','test.cpp','test.py','check.cpp','check.py','gen_test.py']
print('creating',question_name)
os.system('mkdir questions/' + question_name)
os.system('mkdir questions/' + question_name + "/output")
os.system('mkdir questions/' + question_name + "/input")
os.system('mkdir questions/' + question_name + "/images")
for cmd in tch_cmd:
	os.system('touch questions/' + question_name + "/" + cmd)


shutil.copyfile('scripts/gen_test_template.py','questions/' + question_name + '/gen_test.py')
shutil.copyfile('scripts/test_template.py','questions/' + question_name + '/test.py')


print('created '+ question_name);