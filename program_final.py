'''
Interface of the exam
'''

import setup
import program_two
import program_one
import sys
def main(args):
    cand_ls = program_two.main(args)
    if cand_ls == None:
        return None
    sid = str(input("Enter your student identification number (SID) to start exam: "))
    valid = False
    try:                    
        if isinstance(sid,str):
            if len(sid) == 9:
                if int(sid) > 0:
                    valid = True
    except:
        valid = False
    c = 0
    while valid == False:
        c += 1
        print("Invalid SID.")
        if c == 3:
            print("Contact exam administrator.")
            return None
        sid = str(input("Enter your student identification number (SID) to start exam: "))
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
        c = 0
        c2 = 0
        found = False
        while i < len(cand_ls):
            if cand_ls[i].sid == sid:
                found = True
                ind = i
            i += 1
        while not found:
            c += 1
            print("Candidate number not found for exam.")
            choice = str(input("Do you want to try again [Y|N]? "))
            if c == 3:
                print("Contact exam administrator.")
                return None
            c1 = 0
            while choice.lower() != "y" and choice.lower() != "n":
                c1 += 1
                print("Response must be [Y|N].")
                choice = str(input("Do you want to try again [Y|N]? "))
                if c1 == 3:
                    print("Contact exam administrator.")
                    return None
            if choice.lower() == "y":
                c2 += 1
                if c2 == 3:
                    print("Contact exam administrator.")
                    return None
                sid = str(input("Enter your student identification number (SID) to start exam: "))
                valid = False
                try:                    
                    if isinstance(sid,str):
                        if len(sid) == 9:
                            if int(sid) > 0:
                                valid = True
                except:
                    valid = False
                if valid == False:
                    print("Invalid SID.")
                    sid = str(input("Enter your student identification number (SID) to start exam: "))
                i = 0
                found = False
                while i < len(cand_ls):
                    if cand_ls[i].sid == sid:
                        found = True
                        ind = i
                    i += 1
            else:
                return None
        print("Verifying candidate details...")
        name = str(input("Enter your full name as given during registration of exam: "))
        c = 0
        while cand_ls[ind].name.lower() != name.lower():
            c += 1
            if c == 3:
                print("Contact exam administrator to verify documents.")
                return None
            print("Name does not match records.")
            name = str(input("Enter your full name as given during registration of exam: "))
        print("Start exam....")
        print()
        cand_ls[ind].do_exam(False)


            
            
        

        





if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
