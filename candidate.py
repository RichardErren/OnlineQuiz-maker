class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        return self.exam.duration + self.extra_time
            
    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        try:
            if isinstance(sid,str):
                if len(sid) == 9:
                    if int(sid) > 0:
                        self.sid = sid
        except:
            return None

    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        if isinstance(t,int):
            if t > 0:
                self.extra_time = t
    
    def set_confirm_details(self, sid, name):
        '''
        Update attribute confim_details
        '''
        if self.sid == sid and self.name == name:
            self.confirm_details = True
            return True
        else:
            return False

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        import os
        try:
            fobj = f"{self.exam.path_to_dir}/submissions/{self.sid}.txt"
            f = open(fobj, "w")
            f.write(data)
            f.close()
        except:
            cur = os.getcwd()
            os.chdir(self.exam.path_to_dir)
            os.mkdir("submissions")
            os.chdir(cur)
            fobj = f"{self.exam.path_to_dir}/submissions/{self.sid}.txt"
            f = open(fobj, "w")
            f.write(data)
            f.close()   
    
    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details == True:
            self.results = ls

    def do_exam(self, preview=True):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''
        data = ""
        print(f'Candidate: {self.name}({self.sid})')
        t = self.get_duration()
        print(f'Exam duration: {t} minutes')
        print(f'You have {t} minutes to complete the exam.')
        print(self.exam.get_name())

        if self.exam is not None:
            i = 1
            n = len(self.exam.questions)
            while i < n:
                answer = "Answer"
                question = self.exam.questions[i - 1]
                if question.qtype == "multiple":
                    answer = "Answers"
                print(f'Question {i} - {question.qtype.capitalize()} {answer}[{question.marks}]')
                print(question.description)

                j = 0
                while j < len(question.answer_options):
                    print(question.answer_options[j][0])
                    j += 1

                if not preview:
                    response = input(f"Response for Question {i}: ")
                    print()

                    marks = self.exam.questions[i - 1].mark_response(response)

                    data += f"Question {i} - {question.qtype.capitalize()} {answer}[{question.marks}]\n"
                    j = 0
                    data += f"{question.description}\n"
                    while j < len(question.answer_options):
                        data += f"{question.answer_options[j][0]}\n"
                        j += 1
                    data += f"Response for Question {i}: {response}\n"
                    data += f"You have scored {marks:.2f} marks.\n\n"  
                    if i+1 == n:
                        data += "-End-"
                    self.log_attempt(data)  
                else:
                    print(f"Response for Question {i}: \n")
                i += 1
            print('-End-')
       
    def __str__(self):
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out

