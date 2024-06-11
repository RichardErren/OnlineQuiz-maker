'''
Write instructions to execute your test program here.
'''
import question
'''
Initialising the questions and correct answers for the questions to be tested
'''
Q1 = question.Question("short") 
Q2 = question.Question("single") 
Q3 = question.Question("multiple")
Q1.set_correct_answer("Hello")
Q1.set_marks(1)
Q2.set_correct_answer("A")
Q2.set_marks(1)
Q3.set_correct_answer("A, C")
Q3.set_marks(2)

'''
Using assert to test if the expected value matches the value we got
''' 
assert Q1.mark_response("Hello") == 1, "Testcase 1 failed"
print("Testcase 1 passed")
assert Q1.mark_response(2) == 0, "Testcase 2 failed"
print("Testcase 2 passed")
assert Q2.mark_response("A") == 1, "Testcase 3 failed"
print("Testcase 3 passed")
assert Q2.mark_response("E") == 0, "Testcase 4 failed"
print("Testcase 4 passed")
assert Q2.mark_response(3) == 0, "Testcase 5 failed"
print("Testcase 5 passed")
assert Q3.mark_response("A, C") == 2, "Testcase 6 failed"
print("Testcase 6 passed")
assert Q3.mark_response("A, B") == 1, "Testcase 7 failed"
print("Testcase 7 passed")
assert Q3.mark_response("A and B") == 0, "Testcase 8 failed"
print("Testcase 8 passed")
