class Question:
    
    def __init__(self, qtype):
        # you'll need to check if qtype is valid before assigning it
        if self.set_type(qtype) == True:
            self.qtype = qtype
        else:
            self.qtype = None
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None
       
    def set_type(self, qtype):
        if qtype.lower() == 'single' or qtype.lower() == 'multiple' or qtype.lower() == 'short' or qtype.lower() == "end":
            self.qtype = qtype
            return True
        else: 
            self.qtype = None
            return False
    
    def set_description(self, desc):
        if self.qtype == 'end':
            return False
        else:
            if isinstance(desc, str):
                if desc != "":
                    self.description = desc
                    return True
        return False
    
    def set_correct_answer(self, ans):
        if self.qtype == 'end':
            return False
        else:
            if self.qtype.lower() == "short":
                self.correct_answer = ans
                return True
            elif self.qtype.lower() == "single":
                if isinstance(ans, str):
                    if ans.lower() == "a" or ans.lower() == "b" or ans.lower() == "c" or ans.lower() == "d":
                        self.correct_answer = ans
                        return True
            elif self.qtype.lower() == "multiple":
                if isinstance(ans, str):
                    ans1 = ans.replace(" ", "")
                    ans1_ls = ans1.split(",")
                    MaxIndex = len(ans1_ls)
                    i = 0
                    while i < MaxIndex:
                        if not(ans1_ls[i].lower() == 'a' or ans1_ls[i].lower() == 'b' or ans1_ls[i].lower() == 'c' or ans1_ls[i].lower() == 'd'):
                            return False
                        i += 1
                    self.correct_answer = ans
                    return True
        return False
    
    def set_marks(self, num):
        if self.qtype == 'end':
            return False
        else:
            if isinstance(num,int) and num >= 0:
                self.marks = num
                return True
        return False
    
    def set_answer_options(self, opts):
        """
        Update instance variable answer_options.

        opts should have all flags equal to False when passed in.
        This method will update the flags based on the correct answer.
        Only then do we check that the number of correct answers is correct.
        """
        if self.qtype.lower() == "short" or self.qtype.lower() == "end":
            self.answer_options = opts
            return True
        else:
            if isinstance(opts, list):
                if len(opts) != 4:
                    return False
                i = 0
                while i < len(opts):
                    if len(opts[i]) != 2:
                        return False
                    else:
                        if not(isinstance(opts[i], tuple)) or opts[i][1] != False:
                            return False
                    i += 1
                i = 0
                c = 0
                while i < len(opts):
                    if opts[i][0][:2] == "A." or opts[i][0][:2] == "B." or opts[i][0][:2] == "C." or opts[i][0][:2] == "D.":
                        if i == 0:
                            if opts[i][0][0] != "A":
                                return False
                        if i == 1:
                            if opts[i][0][0] != "B":
                                return False
                        if i == 2:
                            if opts[i][0][0] != "C":
                                return False
                        if i == 3:
                            if opts[i][0][0] != "D":
                                return False
                        c += 1
                    i += 1
                if c != 4:
                    return False
                if isinstance(self.correct_answer,str) == False:
                    return False
                else:
                    if self.qtype.lower() == "single":
                        if not(self.correct_answer.lower() == "a" or self.correct_answer.lower() == "b" or self.correct_answer.lower() == "c" or self.correct_answer.lower() == "d"):
                            return False
                        else:
                            i = 0
                            while i < len(opts):
                                if opts[i][0][0].lower() == self.correct_answer.lower():
                                    opts[i] = (opts[i][0],True)
                                i += 1
                            self.answer_options = opts
                            return True
                    if self.qtype.lower() == "multiple":
                        ans1 = self.correct_answer.replace(" ", "")
                        ans1_ls = ans1.split(",")
                        MaxIndex = len(ans1_ls)
                        i = 0
                        while i < MaxIndex:
                            if not(ans1_ls[i].lower() == 'a' or ans1_ls[i].lower() == 'b' or ans1_ls[i].lower() == 'c' or ans1_ls[i].lower() == 'd'):
                                return False
                            i += 1
                        i = 0
                        ans = self.correct_answer.replace(" ", "")
                        ans_ls = ans.split(",")
                        while i < 4:
                            j = 0
                            while j < len(ans_ls):
                                if opts[i][0][0].lower() == ans_ls[j].lower():
                                    opts[i] = (opts[i][0],True)
                                j += 1
                            i += 1
                        self.answer_options = opts
                        return True

            return False
        return False

    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line.
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        if self.qtype == "end" or self.qtype == "short":
            return ""
        else:
            i = 0
            description = ""
            while i < len(self.answer_options):
                if i == 3:
                    description += self.answer_options[i][0]
                else:
                    description += self.answer_options[i][0] + "\n"
                i += 1
            return description

    def mark_response(self, response):
        """
        Check if response matches the expected answer
        Parameter:
            response: str, response provided by candidate
        Returns:
            marks: int|float, marks awarded for the response.
        """
        if self.qtype.lower() == "end":
            return None
        if isinstance(response, int):
            return 0
        if self.qtype.lower() == "single" or self.qtype == "short":
            if response.lower() == self.correct_answer.lower():
                return self.marks
            else:
                return 0
        if self.qtype == "multiple":
            correct = self.correct_answer.replace(" ","")
            correct = correct.split(",")
            Total = len(correct)
            mark = 0
            response = response.replace(" ","")
            resp = response.split(",")
            i = 0
            while i < len(resp):
                j = 0
                while j < len(correct):
                    if resp[i].lower() == correct[j].lower():
                        mark += 1
                    j += 1
                i += 1
            TotalMark = (mark/Total) * self.marks
            return TotalMark

            

    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        if self.qtype == "end":
            return "-End-"
        else:
            preview = ""
            if i == 0:
                i = "X"
            if self.qtype.lower() == "single":
                if show == True:
                    preview += f"Question {i} - Single Answer[{self.marks}]\n"
                    preview += self.description + "\n"
                    preview += self.get_answer_option_descriptions() + "\n"
                    preview += f"Expected Answer: {self.correct_answer}"
                    return preview
                else:
                    preview += f"Question {i} - Single Answer[{self.marks}]\n"
                    preview += self.description + "\n"
                    preview += self.get_answer_option_descriptions()
                    return preview
            elif self.qtype.lower() == "multiple":
                if show == True:
                    preview += f"Question {i} - Multiple Answers[{self.marks}]\n"
                    preview += self.description + "\n"
                    preview += self.get_answer_option_descriptions() + "\n"
                    preview += f"Expected Answer: {self.correct_answer}"
                    return preview
                else:
                    preview += f"Question {i} - Multiple Answers[{self.marks}]\n"
                    preview += self.description + "\n"
                    preview += self.get_answer_option_descriptions()
                    return preview
            else:
                if show == True:
                    preview += f"Question {i} - Short Answer[{self.marks}]\n"
                    preview += self.description + "\n"
                    preview += f"Expected Answer: {self.correct_answer}"
                    return preview
                else:
                    preview += f"Question {i} - Short Answer[{self.marks}]\n"
                    preview += self.description + "\n"
                    preview += self.get_answer_option_descriptions()
                    return preview


    def generate_order():
        """
        Returns a list of 4 integers between 0 and 3 inclusive to determine order.

        Sample usage:
        >>> generate_order()
            [3,1,0,2]
        """
        import random
        ls = []
        i = 0
        while i < 4:
            duplicate = True
            while duplicate == True:
                num = random.randint(0,3)
                duplicate = False
                j = 0
                while j < len(ls):
                    if num == ls[j]:
                        duplicate = True
                    j += 1
            ls.append(num)
            i += 1
        return ls

    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.
        Must call generate_order only once.
        """
        new_order = Question.generate_order()
        ans_options = []
        if self.qtype.lower() == "single":
            i = 0
            while i < 4:
                j = 0
                while j < 4:
                    if new_order[i] == j:
                        ans_options.append(self.answer_options[j])
                    j += 1
                i += 1
            ans_options[0] = (("A." + str(ans_options[0][0][2:])),ans_options[0][1])
            ans_options[1] = (("B." + str(ans_options[1][0][2:])),ans_options[1][1])
            ans_options[2] = (("C." + str(ans_options[2][0][2:])),ans_options[2][1])
            ans_options[3] = (("D." + str(ans_options[3][0][2:])),ans_options[3][1])
            i = 0
            self.answer_options = ans_options
            while i < 4:
                if ans_options[i][1] == True:
                    self.correct_answer = ans_options[i][0][0]
                i += 1
        elif self.qtype.lower() == "multiple":
            i = 0
            while i < 4:
                j = 0
                while j < 4:
                    if new_order[i] == j:
                        ans_options.append(self.answer_options[j])
                    j += 1
                i += 1
            ans_options[0] = (("A." + str(ans_options[0][0][2:])),ans_options[0][1])
            ans_options[1] = (("B." + str(ans_options[1][0][2:])),ans_options[1][1])
            ans_options[2] = (("C." + str(ans_options[2][0][2:])),ans_options[2][1])
            ans_options[3] = (("D." + str(ans_options[3][0][2:])),ans_options[3][1])
            self.answer_options = ans_options
            correct_ans = []
            i = 0
            while i < 4:
                if ans_options[i][1] == True:
                    correct_ans.append(ans_options[i][0][0])
                i += 1
            j = 0
            new_correct = ""
            while j < len(correct_ans):
                if j == len(correct_ans)-1:
                    new_correct += correct_ans[j]
                    break
                new_correct += correct_ans[j] + ", "
                j += 1
            self.correct_answer = new_correct
    
    def copy_question(self):
        new_question = Question(self.qtype)
        new_question.set_description(self.description)
        new_question.set_correct_answer(self.correct_answer)
        new_question.set_marks(self.marks)
        new_ans_opt = []
        i = 0
        while i < len(self.answer_options):
            new_ans_opt.append((self.answer_options[i][0],False))
            i += 1
        new_question.set_answer_options(new_ans_opt)
        return new_question

      

    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''
