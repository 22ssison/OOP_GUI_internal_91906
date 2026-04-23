"""
NCEA Level 3 Chemistry Quiz: Properties of Organic Compounds
------------------------------------------------------------
An interactive GUI application developed using Tkinter and OOP principles.
This program evaluates knowledge of organic functional groups and reactions 
through a dynamic multiple-choice interface.
"""


class Question:
    def __init__(self, txt, options, ans_index, marks):
        self.text = text # question
        self.options = options # different options in list
        self.ans_index = ans_index # index of correct answer
        self.marks = marks # how many marks the question is worth

class OrgQuiz:
    def __init__(self, parent):
        self.questions = [ 
            Question("")]