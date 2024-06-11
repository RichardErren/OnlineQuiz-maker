'''
Interface of the exam
'''

import sys
import setup
import program_one

def assign_exam(exam_obj):
    f = f"{exam_obj.path_to_dir}/students.csv"
    fobj = open(f,"r")
    cand_ls = setup.extract_students(fobj)
    if cand_ls == []:
        print("No candidates found in the file")
        return None
    print("Assigning exam to candidates...")
    shuffle_flag = exam_obj.shuffle
    if shuffle_flag == True:
        i = 0
        while i < len(cand_ls):
            new_exam = exam_obj.copy_exam()
            j = 0
            while j < len(new_exam.questions)-1:
                if len(new_exam.questions[j].answer_options) != 0:
                    new_exam.questions[j].shuffle_answers()
                j += 1
            cand_ls[i].exam = new_exam
            i += 1
    else:
        i = 0
        while i < len(cand_ls):
            new_exam = exam_obj.copy_exam()
            cand_ls[i].exam = new_exam
            i += 1
    print(f"Complete. Exam allocated to {len(cand_ls)} candidates.")
    return cand_ls

def main(args):
    exam_obj = program_one.main(args)
    if exam_obj != False:
        cand_ls = assign_exam(exam_obj)
        sid = str(input("Enter SID to preview student's exam (-q to quit): "))
        while sid != "-q":
            if sid == "-a":
                i = 0
                while i < len(cand_ls):
                    cand_ls[i].do_exam()
                    print()
                    i += 1
            else:
                valid = False
                try:
                    if isinstance(sid,str):
                        if len(sid) == 9:
                            if int(sid) > 0:
                                valid = True
                except:
                    valid = False
                if valid:
                    i = 0
                    found = False
                    while i < len(cand_ls):
                        if cand_ls[i].sid == sid:
                            found = True
                            ind = i
                        i += 1
                    if found == False:
                        print("SID not found in list of candidates.")
                        print()
                    else:
                        cand_ls[ind].do_exam()
                        print()
                else:
                    print("SID is invalid.")
                    print()
            sid = str(input("Enter SID to preview student's exam (-q to quit): "))
        return cand_ls



if __name__ == "__main__":
    main(sys.argv)
