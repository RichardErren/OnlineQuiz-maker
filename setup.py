'''
Functions to setup the exam questions and candidate list for the exam.
'''
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step).
    2. You'll need to convert the possible answers (if any) to a list of tuples (see 
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    question_ls = []
    desc_ls = []
    ans_options_ls = []
    exp_ans = []
    marks_ls = []
    ls_qtype = []
    line = 0
    flag1 = False
    flag2 = False
    while line != "":
        desc = ""
        ans_options = []
        while True:
            line = fobj.readline()
            line1 = line.strip()
            if line1 == "":
                break
            line = line.strip()
            if line[:17].lower() == "expected answer: ":
                flag1 = False
                flag2 = False
                exp_ans.append(line[17:])
            if line[:7].lower() == "marks: ":
                try:
                    marks_ls.append(int(line[7:]))
                except ValueError:
                    marks_ls.append(line[7:])
            if flag2 == True:
                ans_options.append((line, False))
            if line[:8].lower() == "possible":
                flag1 = False
                flag2 = True
            if flag1 == True:
                desc += line + "\n"
            if line[:11] == "Question - ":
                ls_qtype.append(line[11:].lower())
                qtype = line[11:].lower()
                flag1 = True
        question_ls.append(question.Question(qtype))
        desc_ls.append(desc.rstrip("\n"))
        ans_options_ls.append(ans_options)
    i = 0
    if len(exp_ans) < len(question_ls):
        exp_ans.append("")
    while i < len(question_ls):
        question_ls[i].set_description(desc_ls[i])
        question_ls[i].set_correct_answer(exp_ans[i])
        question_ls[i].set_answer_options(ans_options_ls[i])
        question_ls[i].set_marks(marks_ls[i])
        i += 1
    question_ls.append(question.Question("end"))
    return question_ls



def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.

    Sample usage:
    >>> to_sort = [(1.50, "orange"), (1.02, "apples"), (10.40, "strawberries")]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: [(1.5, 'orange'), (1.02, 'apples'), (10.4, 'strawberries')]
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: [(1.02, 'apples'), (1.5, 'orange'), (10.4, 'strawberries')]
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: [(10.4, 'strawberries'), (1.5, 'orange'), (1.02, 'apples')]
    >>> to_sort = [ "oranges", "apples", "strawberries"]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: ['oranges', 'apples', 'strawberries']
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: ['apples', 'oranges', 'strawberries']
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: ['strawberries', 'oranges', 'apples']
    """
    if order == 0:
        return to_sort
    elif order == 1:
        n = len(to_sort)
        swap = False
        i = 0
        while i < n-1:
            j = 0
            while j < n-i-1:
                if to_sort[j] > to_sort[j+1]:
                    swap = True
                    temp = to_sort[j]
                    to_sort[j] = to_sort[j+1]
                    to_sort[j+1] = temp
                j += 1
            if swap == False:
                break
            i += 1
        return to_sort
    elif order == 2:
        n = len(to_sort)
        swap = False
        i = 0
        while i < n-1:
            j = 0
            while j < n-i-1:
                if to_sort[j] > to_sort[j+1]:
                    swap = True
                    temp = to_sort[j]
                    to_sort[j] = to_sort[j+1]
                    to_sort[j+1] = temp
                j += 1
            if swap == False:
                break
            i += 1
        i = n-1
        new_sort = []
        while i >= 0:
            new_sort.append(to_sort[i])
            i -= 1 
        return new_sort
    else:
        return to_sort

def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    cand = []
    try:
        lines = fobj.readlines()
        i = 1
        while i < len(lines):
            line = lines[i]
            line = line.strip()
            line = line.split(",")
            if line[2] == "":
                line[2] = 0
            cand.append((line[0],line[1],int(line[2])))
            i += 1
        cand_ls = sort(cand,1)
        i = 0
        cand = []
        while i < len(cand_ls):
            cand.append(candidate.Candidate(cand_ls[i][0],cand_ls[i][1],cand_ls[i][2]))
            i += 1
        return cand
    except:
        return []
        
