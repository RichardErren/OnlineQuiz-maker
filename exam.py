class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)

    def set_name(self, path):
        """
        Sets the name of the exam. 
        """
        path = path.split("/")
        name = path[(len(path)-1)]
        name = name.replace(" ","_")
        self.name = name

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        name = self.name.replace("_", " ").upper()
        return name

    
    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if self.questions != []:
            self.exam_status = True
        
    
    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if t > 0:
            self.duration = t

    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''
        if not(isinstance(ls, list)):
            return False
        else:
            i = 0
            j = len(ls) - 1
            if ls[j].qtype.lower() != "end":
                print("End marker missing or invalid")
                return False
            else:
                if ls[j].description != None or ls[j].correct_answer != None or len(ls[j].answer_options) != 0:
                    print("End marker missing or invalid")
                    return False
            while i < (len(ls) - 1):
                if ls[i].qtype.lower() == "end":
                    print("End marker missing or invalid")
                    return False
                else:
                    if ls[i].description == None or ls[i].description == "" or ls[i].correct_answer == "" or ls[i].correct_answer == None:
                        print("Description or correct answer missing")
                        return False
                    elif ls[i].qtype.lower() == "short":
                        if len(ls[i].answer_options) != 0:
                            print("Answer options should not exist")
                            return False
                    else:
                        if len(ls[i].answer_options) == 0:
                            print("Answer options incorrect quantity")
                            return False
                        elif len(ls[i].answer_options) != 4:
                            print("Answer options incorrect quantity")
                            return False
                i += 1
            self.questions = ls
            return True
                    


    
    def preview_exam(self):
        '''
        Returns a formatted string.
        '''
        preview = self.get_name() + "\n"
        i = 0
        while i < len(self.questions):
            preview += self.questions[i].preview_question(i+1) + "\n\n"
            i += 1
        return preview
    
    def copy_exam(self):
        '''
        Create a new exam object using the values of this instances' values.
        '''
        from question import Question
        # TODO: make a new exam object (call the constructor)
        new_exam = Exam(self.duration,self.path_to_dir,self.shuffle)
        new_exam.set_name(self.name)

        # make a new list of questions to reassign to the attribute
        new_questions = []
        i = 0
        while i < len(self.questions):
            original_question = self.questions[i]
            # call the copy method for this question
            # TODO: (you'll need to write this instance method in Question)
            new_question = original_question.copy_question()

            # insert this into new list of questions
            new_questions.append(new_question)
            i += 1

        # TODO: assign this new question list to the new exam
        new_exam.set_questions(new_questions)

        # return the new exam
        return new_exam


    def __str__(self):
        pass
