# qtool
python tool to make questions and run and make  testcases for algorithm problems

# Run 
- Clone this repo
- Go to the root directory
- Run scripts/create_ques.py
- Give details
- This will create a boilerplate question structure in the questions folder
- Directory structure is given below
```
folder of question (name : q_<question_name>):
		question.txt
			-output-folder
				output<ij>.txt
			-input-folder
				input<ij>.txt
			solution.cpp
			solution.py
			test.cpp or test.py /// generarte test case code
			editorial.txt or editorial.md
			comments.txt 
			check.cpp or check.py /// generate checking of output
      gen_test.py // helper function to generate testcases
 
 ```
 
 # Generate testcases
 - After creating question through create_ques.py
 - Create solution.cpp and compile and create solution.out
 - Now go to test.py and complete the test functions
 - Now run gen_test.py with command line arguments
 - For generating input ``` gen_test.py in```
 - For generating output ``` gen_test.py out```
