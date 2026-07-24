class QuizBrain:
    def __init__(self,question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0
        self.total_score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)


    def next_question(self):
        current = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q{self.question_num} {current.text} True/False ")
        self.check_answer(user_answer,current.answer)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it")
            self.score += 1
            self.total_score +=1
            print(f"Current Score is {self.score}/{self.total_score} ")
        else:
            print("You got it wrong")
            self.score = self.score
            self.total_score += 1
            print(f"Current Score is {self.score}/{self.total_score} ")
        print(f"Correct answer is {correct_answer}.")


