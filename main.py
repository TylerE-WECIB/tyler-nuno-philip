class Questions:
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        self.question_id = question_id
        self.question_text = question_text
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.correct_answer = correct_answer
        self.question_subject = None


class PythonQuestions(Questions):
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        super().__init__(question_id, question_text, answer_1, answer_2, answer_3, correct_answer)
        Questions.question_subject = "Python"


class CtiQuestions(Questions):
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        super().__init__(question_id, question_text, answer_1, answer_2, answer_3, correct_answer)
        Questions.question_subject = "CTI"