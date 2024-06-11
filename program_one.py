'''
Interface of the exam
'''

import setup
import sys

def parse_cmd_args(args):
    '''
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam

    >>> parse_cmd_args(['program.py', '/home/info1110/', '60', '-r'])
    ('/home/info1110/', 60, True)

    >>> parse_cmd_args(['program.py', '/home/info1110/', 'ab', '-r'])
    Duration must be an integer

    >>> parse_cmd_args(['program.py', '/home/info1110/'])
    Check command line arguments
    '''
    if len(args) >= 3:
        name = args[1]
        dur = args[2]
        try:
            dur = int(dur)
        except ValueError:
            print("Duration must be an integer")
            return None
        flag = False
        if len(args) > 3:
            if args[3] == "-r":
                flag = True
        return (name, dur, flag)
    else:
        print("Check command line arguments")
        return None
            



def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file 
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
    '''
    f = f"{obj.path_to_dir}/questions.txt"
    fobj = open(f,"r")
    questions_ls = setup.extract_questions(fobj)
    if obj.set_questions(questions_ls):
        obj.set_exam_status()
        return (obj, True)
    else:
        return (obj, False)


def main(args):
    '''
    Implement all stages of exam process.
    '''
    from exam import Exam 
    arg = parse_cmd_args(args)
    if arg == None:
        return False
    path_name, duration, shuffle = arg
    try:
        file1 = f"{path_name}/questions.txt"
        fobj1 = open(file1,"r")
        file2 = f"{path_name}/students.csv"
        fobj2 = open(file2,"r")
    except FileNotFoundError:
        print("Missing files")
        return False
    print("Setting up exam...")
    exam1 = Exam(duration,path_name,shuffle)
    (exam1,complete) = setup_exam(exam1)
    if complete == False:
        print("Error setting up exam")
        return False
    print("Exam is ready...")
    choice = str(input("Do you want to preview the exam [Y|N]? "))
    while choice.lower() != "y" and choice.lower() != "n":
        print("Invalid command.")
        choice = str(input("Do you want to preview the exam [Y|N]? "))
    while choice.lower() == "y":
        print(exam1.preview_exam(),end = "")
        choice = str(input("Do you want to preview the exam [Y|N]? "))
        while choice.lower() != "y" and choice.lower() != "n":
            print("Invalid command.")
            choice = str(input("Do you want to preview the exam [Y|N]? "))
    return exam1



if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
