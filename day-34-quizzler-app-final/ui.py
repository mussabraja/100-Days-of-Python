
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title('Quizzler by Mussab')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.quiz = quiz_brain
        self.image_tick = PhotoImage(file="images/true.png")
        self.image_cross = PhotoImage(file="images/false.png")
        self.canvas = Canvas(width=300,height=250,bg='white',highlightthickness=0)
        self.scoretext = self.canvas.create_text(150,20,text=f'Score {self.quiz.score}')
        self.text = self.canvas.create_text(
            150, 125,
            width=280,
            text=self.quiz.next_question(),
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.button_tick = Button(image=self.image_tick,command=self.check_ans_true)
        self.button_tick.grid(column=0,row=2)
        self.button_cross =Button(image=self.image_cross,command=self.check_ans_false)
        self.button_cross.grid(column=1,row=2)
        self.canvas.grid(column=0,row=1,columnspan=2)
        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=q_text)
            self.canvas.itemconfig(self.scoretext,text=f'Score: {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.text, text='Quiz Ended')
            self.button_tick.config(state="disabled")
            self.button_cross.config(state="disabled")

    def check_ans_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)



    def check_ans_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

