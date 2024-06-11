

dddf# Test Case Designs
Complete the given tables with details of your test case design for each question type.
State the values to initalize appropriate `Question` objects required for the test case.

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail 

Table 1: Summary of test cases for method `mark_response` for question type `short`

| Test ID | Description | Inputs | Expected Output | Status |
| ------- | ----------- | ------ | --------------- | ------ |
|    1    |Positive testcase/string input |"Hello"|1|pass|
|    2    |Negative testcase/integer input|2|-|pass|
|         |             |        |                 |        |

Table 2: Summary of test cases for method `mark_response` for question type `single`

| Test ID | Description | Inputs | Expected Output | Status |
| ------- | ----------- | ------ | --------------- | ------ |
|    3    |Positive testcase/string input of A,B,C or D|"A"|1|pass|
|    4    |Negative testcase/string input of E|"E"|0|pass|
|    5    |Negative testcase/integer input|3|0|pass|

Table 3: Summary of test cases for method `mark_response` for question type `multiple`

| Test ID | Description | Inputs | Expected Output | Status |
| ------- | ----------- | ------ | --------------- | ------ |
|    6    |Positive testcase/String input of combination of A,B,C or D|"A, C"|2|pass|
|    7    |Postitive testcase/string input of combination of A,B,C or D but answer is partially correct|"A, B"|1|pass|
|    8    |Negative testcase/String input invalid format|"A and B"|0|pass|

# 
