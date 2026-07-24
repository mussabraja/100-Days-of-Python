from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for bank in question_data:
    question_text = bank["text"]
    question_answer = bank["answer"]
    question_ask = Question(question_text,question_answer)
    question_bank.append(question_ask)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You have completed the Quiz")
print(f"Your total score is: {quiz.score}/{quiz.total_score}")
